import requests
import smtplib

api_key="48ff60adb41f00921134d1b855f4c2c4"
weather_parameters={
    "lat":"18.666691",
    "lon":"74.150654",
    "appid":api_key,
    "cnt":4
}

response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=weather_parameters)


catch=response.json()
first_catch=catch["list"][0]
second_catch=first_catch["weather"][0]
third_catch=second_catch["id"] 

weather_description=second_catch["description"]

def rain_data_fetcher():
    will_it_rain=False
    for hour_data in catch["list"]:
        condition_codes=hour_data["weather"][0]["id"]
        if int(condition_codes) < 700:
            will_it_rain=True
            break
    if will_it_rain:
        return f"The weather is {weather_description}.So do carry an umbrella"
    else:
        return f"The weather is {weather_description}. No rain expected"
        
        

my_email="yashpatil0710@gmail.com"
security="njja nhai ltad dnnl"

with smtplib.SMTP("smtp.gmail.com",587) as connection: #587 is the only port supported for both encryp an ddecryp at same time
    connection.starttls() 
    #Adds additonal security. 
    # If anyone tries to see this messsage or email then this line encrypts it into non-understandable code

    connection.login(user=my_email,password=security)
    connection.sendmail(from_addr=my_email,
                        to_addrs="yashpatil0710@gmail.com",
                        msg=f"Subject: Rain Predictor \n\n {rain_data_fetcher()}")
    
