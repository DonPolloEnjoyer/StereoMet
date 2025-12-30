import os

from flask import Flask, render_template, request, redirect, url_for, session
# from werkzeug.security import generate_password_hash, check_password_hash
import flask as fk
import json

from to1string import to1str1




app = Flask(__name__)
app.secret_key = os.urandom(24)  # Секретный ключ для сессий

def br_adder(text):
    nt = ""
    for i in text:
        if(i == "\n"):
            nt += "<br>\n"
        else:
            nt += i
    return nt

def sub(subs: list, main: list | str):
    for s in subs:
        if(s in main):
            return True
    return False

def br_lines(opened: list[str]):
    intag = False
    nopen = ""
    for l in opened:
        if sub(["<math", "wobr"], l):
            intag = True
        elif sub(["</math>", "wbr"], l):
            intag = False
        if intag:
            nopen += l
        else:
            nopen += l[:-1] + "<br>\n"
    return nopen


@app.route("/")
def home():
    return render_template("main1.html")

@app.route("/<clas>")
def themes(clas):
    if clas in ["10", "11"]:
        r = open(f"static\\{clas}\\temi.json",
            encoding="utf-8").read()
        l = json.loads(r)
        # print(l)
        return render_template("themes1.html", spis = l, cl = clas)
    return render_template("themes1.html")

@app.route("/<clas>/<nom>")
def tema(clas, nom):
    path = f"static\\{clas}\\{nom}"

    r = open(f"{path}\\tema.json",
        encoding="UTF-8")
    l = json.loads(r.read())

    l['opis'] = br_lines(open(f"{path}\\0.txt", 
        encoding="UTF-8").readlines()[1:])

    for i in range(1, len(l['teor'])+1):
        path2 = f"{path}\\{i}.txt"
        path2_2 = f"{path}\\{i}.html"
        try:
            ftem = open(path2, encoding="UTF-8").readlines()
        except:
            ftem = open(path2_2, encoding="UTF-8").readlines()
        ftem.pop(0)
        l['teor'][i - 1][0] = br_lines(ftem)


    return render_template("tema1.html", tem = l, clas = clas, nom = nom)



if( __name__ == '__main__' ):
    app.run(host = "127.0.0.1", port = 3306, debug = True)


# flask --app app run --host="0.0.0.0" --port=3306 --debug
# , ssl_context = 'adhoc'
# C:\Users\IGOR_PC\Documents\GitHub\StereoMet\app.py



