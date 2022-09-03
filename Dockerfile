FROM python:3.10-alpine

WORKDIR /usr/src/discord-bot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./src/main.py" ]