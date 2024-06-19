#python 100_Greatest_movies_of_all_times.py

import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies_website = response.text

soup = BeautifulSoup(movies_website, "html.parser")

movie_titles = [title.getText() for title in soup.select("h3.title")]
movie_titles = movie_titles[::-1]

# for movie in movie_titles:
	


# goto https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
# if you have "UnicodeEncodeError: 'charmap' codec can't encode characters"
with open("movies.txt", mode="w", encoding="utf-8") as file:
	file.write("TOP) Message\n")
	for movie in movie_titles:
		file.write(f"{movie}\n")
		