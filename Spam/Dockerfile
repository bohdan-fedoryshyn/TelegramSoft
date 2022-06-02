FROM python:3.8-slim

WORKDIR /app

COPY ../General/Login.py Login.py
COPY ../General/db.py db.py
COPY ../General/db_config.json db_config.json

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5003
ENTRYPOINT python3 main.py