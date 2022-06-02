FROM python:3.8-slim

WORKDIR /app

COPY ../Login.py .
COPY ../proxy.json .

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT python3 Spamer.py