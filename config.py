import os
import re

BOT_TOKEN = "7198441390:AAHPvsEWEGpRTuLgo8g0qR0Tx54nPAicr6g"

TELEGRAM_API = "28192191"

TELEGRAM_HASH = "663164abd732848a90e76e25cb9cf54a"

id_pattern = re.compile(r'^.\d+$')

ADMINS = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMINS', '2048030675').split()]
#Bot's usernmae without @
BOT_USERNAME = "terabox_dlrobot_bot"

KEYWORDS = ['nephobox', 'terabox', 'teraboxapp', '1024terabox', '1024tera']

FORCE_MSG = "ʜᴇʟʟᴏ 😊 {first}\n\n<b>Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ Kɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ ᴍʏ Cʜᴀɴɴᴇʟ</b>"

FSUB_ID = "-1002249393777"

#ADMINS = '2048030675'

DUMP_CHAT_ID = "-1002149484754"

DB_URI = "mongodb+srv://file:link@cluster0.jth5g3y.mongodb.net/?retryWrites=true&w=majority"

DB_NAME = "tbcluster"

WAIT_MSG = "Please Wait....."

REPLY_ERROR = "Reply to a message"

LOG_ID = "-1002222452970"

LOG_TEXT = """#ɴᴇᴡ_ᴜꜱᴇʀ

◉ ᴜꜱᴇʀ-ɪᴅ: <code>{id}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {first_name} {last_name}
◉ ᴜꜱᴇʀɴᴀᴍᴇ: @{uname}"""

HELP_TXT = f"""<b>Hᴏᴡ ᴛᴏ Usᴇ?💡</b>
\n<b>Jᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ғɪʀsᴛ ᴀɴᴅ ᴛʜᴇɴ sᴇɴᴅ ᴀɴʏ ᴛᴇʀᴀʙᴏx ʟɪɴᴋ ᴛᴏ ᴛʜᴇ ʙᴏᴛ</b>

\n<b>Rᴇᴀsᴏɴ ғᴏʀ Dᴏᴡɴʟᴏᴀᴅ Fᴀɪʟᴇᴅ🚩</b>
\n<b>Mᴀʏ ʙᴇ ᴅᴜᴇ ᴛᴏ ᴛʜᴇ Fɪʟᴇ sɪᴢᴇ📁 ᴏʀ</b> \n<b>Mᴜʟᴛɪᴘʟᴇ Fɪʟᴇs🗂 ɪɴ ᴛʜᴇ ʟɪɴᴋ ᴏʀ</b>\n<b>ᴅᴜᴇ ᴛᴏ Tᴇʀᴀʙᴏx Eʀʀᴏʀ🚧</b>


\n<b>Bᴏᴛ ᴄᴀɴɴᴏᴛ ᴅᴏᴡɴʟᴏᴀᴅ📥 ʟᴀʀɢᴇʀ ғɪʟᴇs</b>

\n<b>ᴀɴʏ ɪssᴜᴇs ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴠɪᴀ</b> @c0nt4ct_bot"""