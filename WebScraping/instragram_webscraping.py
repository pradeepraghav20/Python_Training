from bs4 import BeautifulSoup
from urllib.request import urlopen
handle="india"
url="https://www.instagram.com/"

try:
    page=urlopen(url+handle).read()
    soup=BeautifulSoup(page,"html.parser")
    # result=requests.get(url+handle)
    # soup=BeautifulSoup(result.content,"html.parser")
    res=soup.find('meta',property="og:description")["content"]
    # print(res)
    list_data=(res.split(','))
    print("***********************")
    print("Insta-Account",url+handle)
    for i in  range (len(list_data)):
        if (i==2):
            print(list_data[i].split('-')[0].strip())
        else:
            print(list_data[i].strip())

except Exception as error:
    print("Unexpected Error",error)

print("***********************\n")
