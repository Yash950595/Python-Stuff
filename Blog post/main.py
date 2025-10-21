from flask import Flask, render_template,request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    if data["name"] and data["email"] and data["phone"] and data["message"]:
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)

my_email="yashpatil0710@gmail.com"
security="njja nhai ltad dnnl"

def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # 587 is the only port supported for both encrypt and decrypt at same time
        connection.starttls()
        connection.login(user=my_email, password=security)
        connection.sendmail(from_addr=my_email,
                           to_addrs="yom141841@gmail.com",
                           msg=f"Subject: New Message \n\n Name: {name} \n Phone Number: {phone} \n Email: {email} \n Message: {message}")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
