import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

respond = requests.get(URL)
soup = BeautifulSoup(respond.text, "html.parser")
titles = soup.findAll(name="h3", class_="title")
text = "".join(title.text+"\n" for title in reversed(titles))

with open("movies.txt", mode="w",encoding="utf-8") as file:
    file.write(text)

