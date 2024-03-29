from flask import Flask, render_template,  redirect, request
from dbworker import *

app = Flask(__name__)
@app.route("/")
def main_site():
    return redirect("/posts")



# @app.route("/logging", methods=["GET", "POST"])
# def loging():
#     if request.method=="POST":
#         name = request.form.get("name")
#         return "HEllo"
#     return render_template("register.html")



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
        print(request.remote_addr)
        if len(content)>=1500 or len(title) >=120 or len(content)==0:
            print(content,title)
            return redirect("/posts")
        else:
            print(len(content)==0)
            print(type(len(content)))
            print(title, content)
            DataBase.add_posts(title, content)
            return redirect("/posts")  
            # return render_template("PublicationDone.html")
    return render_template("add_post.html")


# app.add_url_rule('/', 'index', main_site)
app.run(debug=False)

