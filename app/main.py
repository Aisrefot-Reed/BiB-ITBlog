from flask import Flask, render_template,  redirect
from dbworker import *
# from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)



@app.route("/")
def mainSite():
    data = DataBase.get_all_posts()
    col = len(data)
    return render_template("posts.html", col=col, data=data)

@app.route("/<int:post_id>")
def open_post(post_id):
    
    return f"HAHAH {post_id}"

app.run()

