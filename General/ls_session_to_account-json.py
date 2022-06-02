import json
import os

os.system("ls /srv/TeleSoft/sessions > sessions.txt")

with open("sessions.txt",'r') as f:
    sessions = f.read()

accounts = []
for el in sessions.split("\n"):
    name = el.replace(".session","")
    accounts.append({"session":name,"api_id": 8, "api_hash": "7245de8e747a0d6fbe11f7cc14fcc0bb"})

with open('account.json','w+') as f:
    json.dump(accounts,f)