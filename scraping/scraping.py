import requests
from bs4 import BeautifulSoup

url = "https://www.huasengheng.com/"
res = requests.get(url)
res.encoding = "utf-8"

soup = BeautifulSoup(res.text,'html.parser')

with open('hello.html','w',encoding='utf-8') as file:
    for c in soup.prettify():
        file.write(c)

# for data in soup.find_all('td'):
#     print(data)

print(soup)