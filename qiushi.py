import requests

from bs4 import BeautifulSoup

content = requests.get("https://www.qiushibaike.com").content
soup = BeautifulSoup(content,'html.parser')

for div in soup.find_all('div',{'class':'content'}):
    print(div.text.strip())