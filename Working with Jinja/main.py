from flask import Flask, render_template
import datetime
import requests
from post_model import Post


app = Flask(__name__)
blog_url="https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()
post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    current_year=datetime.datetime.now().year
    return render_template("index.html",year=current_year,all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    current_year = datetime.datetime.now().year
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
