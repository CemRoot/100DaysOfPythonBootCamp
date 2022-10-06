import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
# My HTTP HEADER
MY_HEADER = {
	"Accept-Language": os.getenv("AL"),
	"User-Agent": os.getenv("UA")
}
URL = input("Enter the URL of the blog you want to scrape: ")
BUYING_PRICE = float(input("Enter the buying price: "))

# EMAIL SENDER

from_address = "ip98kpi@gmail.com"
to_address = "samlorem@yahoo.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "AMAZON PRICE ALERT🧨"
msg['From'] = from_address
msg['To'] = to_address

# Create the message (HTML).
html = f"""\
The price of the product in the link below has been reduced. Click to buy now:
<a href="{URL}">Click here</a>
"""

# Record the MIME type - text/html.
part1 = MIMEText(html, 'html')

# Attach parts into message container
msg.attach(part1)

# Credentials
username = 'ip98kpi@gmail.com'
password = os.getenv('GooglePASS')

# Sending the email
# note - this smtp config worked for me,
# I found it googling around, you may have to tweak the # (587) to get yours to work
# URL catcher for the website
try:
	r = requests.get(URL, headers=MY_HEADER)
	soup = BeautifulSoup(r.content, "lxml")
	price = soup.find(name='span', class_='a-offscreen').getText()
	price_without_currency = price.split('$')[1]
	# print(soup.prettify())
	# print(price)
	if float(price_without_currency) < BUYING_PRICE:
		print("Email sent successfully!")
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(from_address, to_address, msg.as_string())
		server.quit()
	else:
		print("The price is still high. No email sent.")
except ValueError:
	print("Invalid URL! Please pay attention to the URL you entered.")

"""
NOTES: Bu uygulama ile birlikte, bir blog sitesindeki fiyatı düşen bir ürünün fiyatını takip edebilirsiniz.
Bu uygulamanın ilerleyen süreçte windows uygulaması olarak geleceğini düşünüyorum.
Şimdilil mail üzerinden gönderim yapmaktadır.
"""
