import smtplib
import datetime as dt
import random

now = dt.datetime.now()
w = now.weekday()
if w==0:
    with open("Day 32 (mail sender)/quotes.txt", "r",encoding="utf-8") as quotes:
        content = quotes.readlines()
        quote = random.choice(content)

    print("Today's motivational quote:", quote) 
    
    my_email="cr.hellrider007@gmail.com"
    security="aqcw rcgq adwu igsl"

    with smtplib.SMTP("smtp.gmail.com",587) as connection: #587 is the only port supported for both encryp an ddecryp at same time
        connection.starttls()  
        connection.login(user=my_email,password=security)
        connection.sendmail(from_addr=my_email,
                            to_addrs="yashpatil0710@gmail.com",
                            msg=f"Subject: Today's Motivatonal Quote \n\n {quote}")

