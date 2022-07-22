import requests
import json
from bs4 import BeautifulSoup
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
page=requests.get(url)
from pprint import pprint 
# print(page.text)
soup=BeautifulSoup(page.text,'html.parser')
# print(soup)
a=soup.find('tbody',class_='lister-list')
#             # b=soup.find('h1').get_text()
#             # c=soup.find('title').get_text()
movie_details_list=a.find_all('tr')
movie_list=[]
for movie in movie_details_list:
    movie_detail={}
    # print(movie)
    Movie_detail=movie.find('td',class_="titleColumn").get_text().strip()
    # print(Movie_detail)
    Rank=Movie_detail[:3].replace('\n','')
    # print(Rank,end=' ')
    movie_detail["Rank"]=Rank
    # movie_Name=Movie_detail.find('a').get_text()
    movie_Name=movie.find('td',class_="titleColumn").a.get_text()
    # print(movie_Name,end='')
    movie_detail["Name"]=movie_Name
    year_of_release=movie.find('td',class_="titleColumn").span.get_text()
    movie_detail['year_of_release']=year_of_release
    # print(year_of_release)
    Link=movie.find('td',class_="titleColumn").a['href']
    Movie_Link='https://www.imdb.com'+Link
    movie_detail['Movie_Link']=Movie_Link
    # print(Movie_Link)
    movie_list.append(movie_detail)
pprint(movie_list)
file=open('Movies_Details.json','w')
json.dump(movie_list,file,indent=4)


