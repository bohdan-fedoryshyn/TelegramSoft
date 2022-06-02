import time

import requests


class SmsActivate:

    status = True

    def __init__(self):
        with open('Token.txt','r') as token_f:
            self.key = token_f.read()


    def get_balanse(self):

        return str(requests.get("https://sms-activate.ru/stubs/handler_api.php?api_key=" + self.key +"&action=getBalance").text)[15:]

    def get_numberTELEGRAM(self):
        print("GET NUMBER")
        myURL = "https://sms-activate.org/stubs/handler_api.php?api_key=" + self.key + "&action=getNumber&service=tg&forward=0&country=1"
        print(myURL)
        while True:
            s = requests.post(myURL)
            print(s.text)
            time.sleep(0.1)
            if "ACCESS_NUMBER" in s.text:
                break

        par = []
        z = 9
        k = 0
        for el in s.text:
            if el == ":":
                par.append(s.text[k + 1:k + 1 + z])
                z = 12
            k += 1
        print(par)
        print(par[0], "    ", par[1])

        requests.get(
            "https://sms-activate.ru/stubs/handler_api.php?api_key=" + self.key + "&action=setStatus&status=1&id=" + par[0])
        self.id = str(par[0])
        return par

    def get_kod(self):
            ### Костиль
            #if self.status:

             #   self.status = False
             #   return '3234'
            #else:
                url = "https://sms-activate.ru/stubs/handler_api.php?api_key=" + self.key + "&action=getStatus&id=" + self.id
                date_start = time.time()
                while True:
                    v = requests.get(url)
                    time.sleep(1)
                    print(v.text)
                    if "STATUS_OK" in v.text:
                        return v.text[v.text.find(':'):]
                        break

                    if time.time() - date_start > 300:
                        print("ПРойшло більше 5 хв")
                        raise Exception("Time")
