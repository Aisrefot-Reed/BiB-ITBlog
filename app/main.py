from flask import Flask, render_template,  redirect, request
from dbworker import *
# from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

@app.route("/")
def main_site():
    return """<a href="/posts">Hllo</a>"""

@app.route("/logging", methods=["GET", "POST"])
def loging():
    if request.method=="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return "HEllo"
    return render_template("register.html")

@app.route("/posts")
def posts():
    data = DataBase.get_all_posts()
    col = len(data)
    return render_template("posts.html", col=col, data=data)

@app.route("/posts/post<int:post_id>")
def open_post(post_id):
    
    return render_template("post.html", post=DataBase.opened_post(post_id=post_id))


@app.route("/posts/addpost", methods=["GET", "POST"])
def add_post():
    if request.method=="POST":
        content = request.form.get("add_post_content")
        title = request.form.get("add_post_title")
        DataBase.add_posts(title, content)
        return "Успешная публикация!!!"
    return render_template("add_post.html")

# app.add_url_rule('/', 'index', main_site)
app.run(debug=True)

