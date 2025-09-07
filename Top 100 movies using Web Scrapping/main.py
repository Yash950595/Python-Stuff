import requests

from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(URL)
web_html=response.text

soup=BeautifulSoup(web_html,"html.parser")
movie_list=soup.find_all("h3",class_="title")
#print(last_movie.get_text())

movies=[]
for movie in movie_list:
    movies.append(movie.get_text())

new_movies_list=movies[::-1]

def final_list():
    return "\n".join(new_movies_list)

with open("movies.txt", "w", encoding="utf-8") as file:
    file.write(final_list())



