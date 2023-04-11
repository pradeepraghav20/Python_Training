from  bs4 import  BeautifulSoup
import requests
import  csv

URL = "http://www.mediastinger.com/dont-breathe-2-2021-after-the-credits/"
r = requests.get(URL)
media=[]
soup = BeautifulSoup(r.content, "html.parser")
#print(BeautifulSoup.prettify(soup))
media_dict={}
tittle=soup.find('h1',attrs={'id':"posttxt"}).text.strip()
media_dict["title"]=tittle
User_Rating=soup.find('div',attrs = {'id':'ratingfirstdiv_id'}).text.strip()
media_dict['rating']=User_Rating
#print(tittle)
duringcredits=soup.find('div',attrs={'class':'post_secwrapper'})

#DURING THE CREDITS
duringcreditsheadingh=duringcredits.findAll('h3')[0].text.strip()
duringcreditstext=duringcredits.findAll('p')[0].text

media_dict['DuringHeading']=duringcreditsheadingh
media_dict['DuringText']=duringcreditstext

#AFTER THE CREDITS
afterthecreditsh=duringcredits.findAll('h3')[1].text.strip()
afterthecreditstext=duringcredits.findAll('p')[1].text

# media_dict[]=
# media_dict[]=
#MOVIE DETAILS
movie_details=soup.find('div',attrs={'class':'post_firstwrapper'})
titles=movie_details.find('div').text
#titles=movie_details.find('span',attrs={'class':'details-titles'}).text
#titles=movie_details.find('div').text.strip()
# print(titles)



media.append(media_dict)
filename = 'media.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['DuringHeading', 'DuringText', 'rating', 'title'])
    w.writeheader()
    for i in media:
        w.writerow(i)
#done


# find('span',attrs={'id':"spancredit"}).text