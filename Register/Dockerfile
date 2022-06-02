FROM python:3.8-slim-buster


WORKDIR /app

COPY Register/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY General/Login.py Login.py
COPY General/db.py db.py
COPY General/db_config.json db_config.json

COPY Register/. .

CMD ["python3","main.py"]
