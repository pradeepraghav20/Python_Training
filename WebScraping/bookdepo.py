from bs4 import BeautifulSoup
import  requests


url = "https://www.bookdepository.com/bestsellers"
r=requests.get(url)
soup=BeautifulSoup(r.content,"lxml")
all_h3 = soup.find_all("h3", class_="title")
print(all_h3)
# print(soup.prettify())