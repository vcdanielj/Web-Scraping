import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Venezuela"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

content_list = soup.find_all("div", class_="vector-toc-text")

content_text = []
for content in content_list:
    content_text.append(content.get_text())

for i in content_text:
    print(i)
