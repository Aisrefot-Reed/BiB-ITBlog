from flask import Flask, render_template,  redirect


app = Flask(__name__)



@app.route("/")
def mainSite():
    return "MAIN"
    # return render_template("Hellooo")

@app.route('/register', methods=['post', 'get'])
def login():
    return render_template('reg.html')

app.run()

