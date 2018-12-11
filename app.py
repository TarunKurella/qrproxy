from flask import Flask, render_template, request
from flask_qrcode import QRcode
import pyrebase
import random
import string
config = {
    'apiKey': "your key",
    'authDomain': "your domain",
    'databaseURL': "your url",
    'projectId': "your id",
    'storageBucket': "your whatever",
    'messagingSenderId': "your whatever"
  }
firebase = pyrebase.initialize_app(config)
db = firebase.database()

app=Flask(__name__)
qrcode = QRcode(app)
@app.route("/")
def index():
    db.child("STUDENTS").remove()
    return render_template("layout.html")



@app.route("/about")
def about():
    
    
    return render_template("about.html",)
                         
                        
                        
@app.route("/start",methods=['POST'])
def start():
    
    first=request.form['username']
    last=request.form['pass']
    db.child("CSE-B").set({"name":first})
    
    return render_template("start.html",
                         namee=first,
                         last_name=last,)

@app.route("/appp",)
def appp():
    randomm = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(32)])
    
    db.child("KEY").set({"key":randomm})
    
    return render_template("app.html",
                         key=randomm,)
                        
@app.route("/finall",)
def finall():
    hello=[]
    names=[]
    db.child("CSE-B").set({"name":'null'})
    db.child("KEY").set({"key":'null'})
    all_users = db.child("STUDENTS").get()
    for user in all_users.each():
    
      hello.append(user.val())

    for user1 in hello:
    
     names.append(user1["ID"])
    
    
    
    return render_template("finall.html",names=names)
                    
app.run()
