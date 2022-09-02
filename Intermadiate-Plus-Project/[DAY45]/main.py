from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
	text = article_tag.getText()
	article_texts.append(text)
	link = article_tag.get("href")
	if "https://" not in link:  # handles case if article has no link
		link = f"https://news.ycombinator.com/{link}"
	article_links.append(link)

list_upvotes = []
subtexts = soup.find_all(name="td", class_="subtext")
for subtext in subtexts:  # handles case if article has zero upvotes
	try:
		upvotes = int(subtext.find(name="span", class_="score").getText().split()[0])
	except AttributeError:
		upvotes = 0
	list_upvotes.append(upvotes)

highest_upvote = max(list_upvotes)
highest_upvote_index = list_upvotes.index(highest_upvote)

print(article_texts[highest_upvote_index])
print(article_links[highest_upvote_index])

#
# with open("website.html", encoding="utf8") as file:
# 	contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # For find something
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
# 	# print(tag.getText())
# 	# Find link our site code
# 	print(tag.getText("href"))
#
# # For heading found
# heading = soup.find(name="h1", id="name")
# print(heading)
