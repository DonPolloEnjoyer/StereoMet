import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import flask as fk

# DATABASE = 'database.db'

app = Flask(__name__)
app.secret_key = "test" #os.urandom(24)  # Секретный ключ для сессий

@app.route("/")
def home():
    return render_template("main1.html")

@app.route("/index1")
def Tohome2():
    return redirect("/")

@app.route("/theme")
def themes():
    return render_template("arttemp1.html")

if( __name__ == '__main__' ):
    app.run(host = "0.0.0.0", port = 3306, debug = True)

# flask --app app run  --port=3306 --debug
# , ssl_context = 'adhoc'


