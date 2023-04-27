from bs4 import  BeautifulSoup
import requests


url=""

r=requests.get("https://github.com/pradeepraghav20")

soup=BeautifulSoup(r.content,"html.parser")

print(soup.div)
print(soup.title)

# print(soup.prettify())