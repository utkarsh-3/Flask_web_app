from flask import Flask, render_template
from flask import *
import sqlite3 


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template ("index.html")

@app.route("/projects")
def projects():   
    return render_template ("projects.html")

@app.route("/activities")
def activities():
    return render_template ("activities.html")

@app.route("/blog", methods=['GET', 'POST'])
def blog():
    print(request.form)
    name1='dummy'
    mail1='dummyuser@gmail.com'
    message1="East and West , This blog is the best"
    if request.method == 'POST':
        print(request.form.values())
        name1 = request.form.get('cName')
        mail1 = request.form.get('cMail')
        message1 = request.form.get('cMessage')
        db=sqlite3.connect("comments.db")
        db.execute('Insert into comments values (? ,?, ?)',(name1,mail1,message1))
    return render_template ("blog.html")

@app.route("/contact", methods=['GET', 'POST'])
def connect():
    print(request.form)
    name1='dummy'
    mail1='dummyuser@gmail.com'
    message1="East and West , This blog is the best"
    if request.method == 'POST':
        print(request.form.values())
        name1 = request.form.get('cName')
        mail1 = request.form.get('cMail')
        message1 = request.form.get('cMessage')
        db=sqlite3.connect("comments.db")
        db.execute('Insert into comments values (? ,?, ?)',(name1,mail1,message1))
    return render_template ("page-contact.html")

@app.route("/category")
def category():
    return render_template ("category.html")

@app.route("/contact")
def contact():
    return render_template ("page-contact.html")



if __name__ == "__main__":
    app.run(debug=True)