import requests
import smtplib
from email.mime.text import MIMEText

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key="WO1W482CTC12H18C"
news_api_key="f49d9059df7a41a488b683d801d21cd2"

   
stock_parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":api_key,
}

response=requests.get(url=STOCK_ENDPOINT,params=stock_parameters)
catch=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in catch.items()]
yesterday_track=data_list[0]
yesterday_close_price=yesterday_track["4. close"]


day_before_yesterday_track=data_list[1]
DBY_close_price=day_before_yesterday_track["4. close"]


difference=float(yesterday_close_price) - float(DBY_close_price)
positive_diff=abs(difference)

percent_diff= (positive_diff/float(yesterday_close_price))*100



if percent_diff > 1:
    news_parameters={
        "apiKey":news_api_key,
        "qInTitle":COMPANY_NAME,
}
    news_response=requests.get(NEWS_ENDPOINT,params=news_parameters)
    articles=news_response.json()["articles"]

    three_articles=articles[:3]
    

my_email="yashpatil0710@gmail.com"
security="njja nhai ltad dnnl"

formatted_articles = "\n\n".join(
    [f"Headline: {a['title']}\nBrief: {a['description']}" for a in three_articles]
)

msg = MIMEText(formatted_articles, "plain", "utf-8")
msg["Subject"] = "Stock Info"
msg["From"] = my_email
msg["To"] = "yashpatil0710@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=security)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="yashpatil0710@gmail.com",
        msg=msg.as_string()
    )



