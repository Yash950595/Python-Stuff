import requests
from bs4 import BeautifulSoup
import smtplib
import re
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.amazon.in/dp/B0DGLSB5NC"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
}


response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 1. Scrape price
price_tag = soup.select_one("span.a-price span.a-offscreen")
if price_tag:
    price_str = price_tag.get_text().replace("$", "").replace(",", "").strip()
    cleaned_price = re.sub(r"[^\d.]", "", price_str)  # "52990.00"
    price_value = float(cleaned_price)
else:
    print("Price element not found – check your selector or bot detection.")
    price_value = None


title_tag = soup.find(id="productTitle")
title = title_tag.get_text().strip() if title_tag else "Unknown Product"


threshold_price = 100000.0  

if price_value is not None and price_value < threshold_price:
    message = f"{title} is now available for ${price_value}!"
    with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port=587) as connection:
        connection.starttls()
        connection.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("EMAIL_ADDRESS"),
            to_addrs=os.getenv("EMAIL_ADDRESS"),
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n\n{URL}".encode("utf-8")
        )
    print("Alert email sent!")
else:
    print("No alert — price is not below threshold or price not found.")

'''
Learnt New !!!
--> import re brings in Pythons regular expressions (regex) module.
    The re module lets you search, match, and manipulate strings using patterns.

'''