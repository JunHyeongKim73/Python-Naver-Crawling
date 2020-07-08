import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

response = requests.get(
    'https://datalab.naver.com/keyword/realtimeList.naver?age=20s&where=main', headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

i = 1
for item in soup.select("span.item_title"):
    print(str(i) + "th : " + item.get_text())
    i += 1
