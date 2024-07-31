import requests
import aria2p
from datetime import datetime
from status import format_progress_bar
from helper import get_video_duration
from moviepy.editor import VideoFileClip
import asyncio
import os, time
import logging


aria2 = aria2p.API(
    
    aria2p.Client(
        host="http://localhost",
        port=6800,
        secret=""
    )
)


async def download_video(url, reply_msg, user_mention, user_id):
    try:
        # Fetch video metadata
        response = requests.get(f"https://teraboxvideodownloader.nepcoderdevs.workers.dev/?url={url}") #timeout=14)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()

        resolutions = data["response"][0]["resolutions"]
        fast_download_link = resolutions["Fast Download"]
        thumbnail_url = data["response"][0]["thumbnail"]
        video_title = data["response"][0]["title"]

        # Start download using aria2
        options = {
            "dir": "/path/to/downloads",   # Specify the download directory
            "file-allocation": "trunc",    # File allocation strategy
            "max-connection-per-server": 4,  # Max connections per server
            "split": 4,                    # Number of splits
            "max-tries": 5,                # Max number of retries
            "retry-wait": 303
        }
        download = aria2.add_uris([fast_download_link],options=options)
        start_time = datetime.now()

        while not download.is_complete:
            download.update()
            percentage = download.progress
            done = download.completed_length
            total_size = download.total_length
            speed = download.download_speed
            eta = download.eta
            elapsed_time_seconds = (datetime.now() - start_time).total_seconds()
            progress_text = format_progress_bar(
                filename=video_title,
                percentage=percentage,
                done=done,
                total_size=total_size,
                status="Downloading",
                eta=eta,
                speed=speed,
                elapsed=elapsed_time_seconds,
                user_mention=user_mention,
                user_id=user_id,
                aria2p_gid=download.gid
            )
            await reply_msg.edit_text(progress_text)
            await asyncio.sleep(2)

        if download.is_complete:
            file_path = download.files[0].path

            # Download and save thumbnail
            thumbnail_path = "thumbnail.jpg"
            thumbnail_response = requests.get(thumbnail_url, timeout=10)
            with open(thumbnail_path, "wb") as thumb_file:
                thumb_file.write(thumbnail_response.content)

            await reply_msg.edit_text("Uploading...")

            return file_path, thumbnail_path, video_title
        else:
            raise Exception("Download failed")

    except requests.RequestException as e:
        # Handle request exceptions, including timeout
        await reply_msg.edit_text(f"Error: {e}")
        raise

    except aria2p.exceptions.Aria2pException as e:
        # Handle aria2 exceptions
        await reply_msg.edit_text(f"Error: {e}")
        raise

    except Exception as e:
        # Handle other exceptions
        await reply_msg.edit_text(f"An unexpected error occurred: {e}")
        raise



async def upload_video(client, file_path: str, thumbnail_path: str, video_title: str, reply_msg, collection_channel_id, user_mention, user_id, message):
    file_size = os.path.getsize(file_path)
    uploaded = 0
    start_time = datetime.now()
    last_update_time = time.time()

    try:
        video_path = str(file_path)
        clip = VideoFileClip(video_path)
        duration = int(clip.duration)  # Duration in seconds
        clip.close()
    except Exception as e:
        logging.warning(f"Error updating progress message: {e}")
        duration = 0




# Convert duration to a formatted string (e.g., "hh.mm:ss")
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    formatted_duration = f"{hours:02}:{minutes:02}:{seconds:02}"



    async def progress(current, total):
        nonlocal uploaded, last_update_time
        uploaded = current
        percentage = (current / total) * 100
        elapsed_time_seconds = (datetime.now() - start_time).total_seconds()
        
        if time.time() - last_update_time > 2:
            progress_text = format_progress_bar(
                filename=video_title,
                percentage=percentage,
                done=current,
                total_size=total,
                status="Uploading",
                eta=(total - current) / (current / elapsed_time_seconds) if current > 0 else 0,
                speed=current / elapsed_time_seconds if current > 0 else 0,
                elapsed=elapsed_time_seconds,
                user_mention=user_mention,
                user_id=user_id,
                aria2p_gid=""
            )
            try:
                await reply_msg.edit_text(progress_text)
                last_update_time = time.time()
            except Exception as e:
                logging.warning(f"Error updating progress message: {e}")
    
    with open(file_path, 'rb') as file:
        collection_message = await client.send_video(
            chat_id=collection_channel_id,
            video=file,
            duration=duration,
            caption=f"🎞ғɪʟᴇ ɴᴀᴍᴇ : {video_title}\n⏰ᴅᴜʀᴀᴛɪᴏɴ : {formatted_duration}\n👤 ᴛᴀsᴋ ʙʏ : {user_mention}\n🔗 ᴜsᴇʀ's ʟɪɴᴋ: tg://user?id={user_id}",
            thumb=thumbnail_path,
            progress=progress
        )
        await client.copy_message(
            chat_id=message.chat.id,
            from_chat_id=collection_channel_id,
            message_id=collection_message.id
        )
        await asyncio.sleep(1)
        await message.delete()
        #await message.reply_sticker("CAACAgIAAxkBAAEZdwRmJhCNfFRnXwR_lVKU1L9F3qzbtAAC4gUAAj-VzApzZV-v3phk4DQE")

    await reply_msg.delete()

    os.remove(file_path)
    os.remove(thumbnail_path)
    return collection_message.id
