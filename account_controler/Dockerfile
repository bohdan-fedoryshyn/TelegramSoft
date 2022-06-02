FROM python:3.8-slim-buster


WORKDIR /app

COPY account_controler/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY General/db.py account_controler/db.py
COPY General/db_config.json account_controler/db_config.json

COPY account_controler/. .

EXPOSE 5052
CMD ["python3","main.py"]
