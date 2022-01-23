import requests
from bs4 import BeautifulSoup

TOKEN = ''
with open('token.txt','r') as file:
    TOKEN = file.read()

def _lineNotify(payload, file=None):
    url = 'https://notify-api.line.me/api/notify'
    token = TOKEN
    headers = {'Authorization': 'Bearer '+token}
    return requests.post(url, headers=headers, data=payload, files=file)


def line_notify_message(message):
    payload = {'message': message}
    return _lineNotify(payload)


# https://ทองคําราคา.com/tag/ราคาทอง-ฮั่วเซ่งเฮง/
url = "https://xn--42cah7d0cxcvbbb9x.com/tag/%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%97%E0%B8%AD%E0%B8%87-%E0%B8%AE%E0%B8%B1%E0%B9%88%E0%B8%A7%E0%B9%80%E0%B8%8B%E0%B9%88%E0%B8%87%E0%B9%80%E0%B8%AE%E0%B8%87/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
status = response.status_code

data_price = soup.find_all("td", {"class": "em bg-em"})
ask_965 = data_price[2].text
bid_965 = data_price[3].text
update_date = soup.find_all("td", {"class": "em bg-span al-l txt-i"})[0].text

if status == 200:
    # print(bid_965,ask_965,update_date)
    goldprice_message = f"ทองแท่ง96.5%\nรับซื้อ : {bid_965}\nขายออก : {ask_965}\nอัพเดตเมื่อ :{update_date} \nฮั่วเซ่งเฮง"
    line_notify_message(goldprice_message)
