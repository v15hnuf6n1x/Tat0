FROM hrishi2861/terabox:latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8070

CMD ["bash", "start.sh"]
