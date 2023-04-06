from bs4 import BeautifulSoup
import requests

city='delhi'

url="https://www.google.com/search?q="+"weather"+city

req=requests.get(url)
soup=BeautifulSoup(req.content,"html.parser")
# print(soup.prettify())

#temp=soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
temp=soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
print(temp)
#sky description

desc=soup.find('div',attrs={'class':'BNeawe tAd8D AP7Wnd'}).text

data=desc.split('\n')
time=data[0]
sky=data[1]
print(time)
print(sky)
# alldiv=soup.findall('div',attrs={'class':'BNeawe s3v9rD AP7Wnd'})
# print(alldiv)