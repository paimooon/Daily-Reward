import requests
import os

ltuid = os.environ.get('LTUID')
ltoken = os.environ.get('LTOKEN')

url = "https://hk4e-api-os.mihoyo.com/event/sol/sign?act_id=e202102251931481&lang=ko-kr"

cookies = {'ltuid': ltuid, 'ltoken': ltoken}

r = requests.post(url, cookies=cookies)
print(r.json()['message'])
