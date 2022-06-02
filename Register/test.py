import json

str = """iPhone 5S:Telegram iOS 5.15.2
iPhone 5:Telegram iOS 5.15.2
iPhone 6:Telegram iOS 5.15.2
iPhone 6S:Telegram iOS 5.15.2
iPhone 7S:Telegram iOS 5.15.2
iPhone 7:Telegram iOS 5.15.1
iPhone 7S:Telegram iOS 5.15.1
iPhone 8:Telegram iOS 5.15.2
iPhone 5S:Telegram iOS 5.15.1
iPhone 5:Telegram iOS 5.15.1
iPhone 6:Telegram iOS 5.15.1
iPhone 6S:Telegram iOS 5.15.1
iPhone 8:Telegram iOS 5.15.1
iPhone 8:Telegram iOS 5.15""".split('\n')

list = []
#for el in str:
#    dt = el.split(':')
#    list.append([dt[0],dt[1]])

with open('account.json','r') as f:
    acc = json.loads(f.read())

for el in acc:
    el["api_id"] = 8
    el["api_hash"] = "7245de8e747a0d6fbe11f7cc14fcc0bb"



with open('account.json','w+') as f:
    json.dump(acc,f)