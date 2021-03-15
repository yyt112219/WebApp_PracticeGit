import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        subject = request.form.get("subject")
        messages = request.form.get("messages")
        # form submit time
        create_time= datetime.datetime.today().strftime("%Y-%m-%d")
        print(email,create_time)
    return render_template("home.html")
'''
@app.route("/patent",methods=["GET","POST"])
def patent():
    # xx

    # yy

    # zz

    kwargs = {
        "xx":xx,
        "yy":yy,
        "zz":zz
    }
    return render_template('project_patent.html',**kwargs)
    '''