FROM python:3.8-slim-buster


WORKDIR /app

COPY Follow/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY General/Login.py Follow/Login.py
COPY General/db.py Follow/db.py
COPY General/db_config.json Follow/db_config.json

COPY Follow/. .

EXPOSE 5002
CMD ["python3","main.py"]
