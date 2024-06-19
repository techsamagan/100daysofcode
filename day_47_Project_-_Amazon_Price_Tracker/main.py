# python main.py
import requests
from bs4 import	BeautifulSoup	
import lxml
import smtplib

headers = {
	"Accept-Language":"en,ru;q=0.9,en-US;q=0.8,ar-EG;q=0.7,ar;q=0.6",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

amazon_url = "https://www.amazon.com/ANYLUV-Light-Blocking-Glasses-Women/dp/B07RGHSMGF/ref=sr_1_4?crid=3LZ16ZLVJJT45&keywords=computer%2Bglasses%2Bmen&qid=1677022483&s=electronics&sprefix=computer%2Bglas%2Celectronics%2C125&sr=1-4&th=1"

response = requests.get(url=amazon_url, headers=headers)
# print(response.content)
soup = BeautifulSoup(response.content, "lxml")

price = float(soup.select_one("span.a-offscreen").getText()[1:])
print(price)

product_title = soup.select_one("span#productTitle").getText()

my_mail = "newacc01222023@gmail.com"
receive_email = "asalamatov@na.edu"
password = "pobbfhlzozcaczmz"

if price<25.00:
	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(my_mail, password)
		connection.sendmail(from_addr=my_mail, to_addrs=receive_email,
							msg=f"Subject:Amazon Price Alert!\n\n{product_title} is now {price}. Previously, It was $24.99.")





