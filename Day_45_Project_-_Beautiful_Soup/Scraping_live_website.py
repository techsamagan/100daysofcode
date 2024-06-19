import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.select("td.title span.titleline a")
# print(articles)
article_texts = []
article_links = []
for article_tag in articles:
	text = article_tag.getText()
	article_texts.append(text)
	link = article_tag.get("href")
	article_links.append(link)

article_upvotes = [int(vote.getText().split()[0]) for vote in soup.find_all(name = "span", class_ = "score")]
# print(article_texts)
print(len(article_texts))
# print(article_links)
print(len(article_links))
# print(article_upvotes)
print(len(article_upvotes))
