import smtplib

my_email="cr.hellrider007@gmail.com"
security="aqcw rcgq adwu igsl"

with smtplib.SMTP("smtp.gmail.com",587) as connection: #587 is the only port supported for both encryp an ddecryp at same time
    connection.starttls() 
    #Adds additonal security. 
    # If anyone tries to see this messsage or email then this line encrypts it into non-understandable code

    connection.login(user=my_email,password=security)
    connection.sendmail(from_addr=my_email,
                        to_addrs="@gmail.com",
                        msg="Subject: EC \n\n ANNA")
    
'''
🔹 Analogy

Think of it like this:

.SMTP() = you walk into the post office.

.starttls() = you move to a secure counter.

.login() = you show your ID.

.sendmail() = you hand over your letter for delivery.
'''

'''
import datetime as dt

now=dt.datetime.now()
m=now.month
w=now.weekday()
print(now)
print(m)
print(w)
'''