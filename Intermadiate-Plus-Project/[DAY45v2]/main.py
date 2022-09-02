import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")
articles = soup.find_all(name="h3", class_="title")
article_texts = []
for article_tag in articles:
	text = article_tag.getText()
	article_texts.append(text)
print(article_texts)
# Save file
with open("movie.txt", "w", encoding="utf-8") as file:
	for text in article_texts:
		file.write(text + "\n")

# Write your code above this line 👆
