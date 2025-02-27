from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from colorama import init, Fore, Back, Style
from tempfile import mkdtemp
import wordfreq
import random
import enchant

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
init()

def listToString(s: list): 
    # initialize an empty string
    str1 = "" 

    # traverse in the string
    for ele in s: 
        str1 += ele

    # return string
    return str1.lower()

d = enchant.Dict('en_US')
loop = True

def pick_random_word():
    word_list = [word for word in wordfreq.top_n_list('en', 5000) if len(word) == 5]
    return random.choice(word_list)

lista = []
certo = 0
check = [""]

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        lista.clear()
        return render_template("index.html")
    else:
        check[0] = ""
        word1 = pick_random_word()
        print(word1)
        letras = []
        letras.append(request.form.get("one"))
        letras.append(request.form.get("two"))
        letras.append(request.form.get("three"))
        letras.append(request.form.get("four"))
        letras.append(request.form.get("five"))
        if d.check(listToString(letras)) == False:
            flash('Invalid Word!')
            check[0] = "."
            return redirect(url_for('index'))
        if check[0] == "":
            lista.append(letras)  
        print(lista)
        session["1"] = lista
        session["word1"] = word1
        session["2"] = certo 
        return redirect(url_for("index2"))
    
@app.route("/index2", methods = ["GET", "POST"])
def index2():
    if request.method == "GET":
        return render_template("index2.html", lista = session["1"], word = session["word1"])
    else:
        check[0] = ""
        word = pick_random_word()
        letras = []
        letras.append(request.form.get("one"))
        letras.append(request.form.get("two"))
        letras.append(request.form.get("three"))
        letras.append(request.form.get("four"))
        letras.append(request.form.get("five"))
        if d.check(listToString(letras)) == False:
            flash('Invalid Word!')
            check[0] = "."
            return redirect(url_for('index2'))
        if check[0] == "":
            lista.append(letras)
        certo = 0
        for i in range(0,5) :
            if lista[1][i].lower() == session["word1"][i].lower():
                certo = certo + 1
        if certo == 5:
            return redirect(url_for("index7"))
        print(lista)
        session["1"] = lista
        return redirect(url_for("index3") )
    
@app.route("/index3", methods = ["GET", "POST"])
def index3():
    if request.method == "GET":
        return render_template("index3.html", lista=session["1"], word=session["word1"],certo=session["2"])
    else:
        check[0] = ""
        word = pick_random_word()
        letras = []
        letras.append(request.form.get("one"))
        letras.append(request.form.get("two"))
        letras.append(request.form.get("three"))
        letras.append(request.form.get("four"))
        letras.append(request.form.get("five"))
        if d.check(listToString(letras)) == False:
            flash('Invalid Word!')
            check[0] = "."
            return redirect(url_for('index3'))
        if check[0] == "":
            lista.append(letras)
        certo=0
        for i in range(0,5) :
            if lista[2][i].lower() == session["word1"][i].lower():
                certo = certo + 1
        if certo == 5:
            return redirect(url_for("index7"))
        print(certo)
        print(lista)
        session["1"] = lista
        return redirect(url_for("index4") )
    
@app.route("/index4", methods = ["GET", "POST"])
def index4():
    if request.method == "GET":
        return render_template("index4.html", lista=session["1"], word = session["word1"],certo = session["2"])
    else:
        check[0] = ""
        word = pick_random_word()
        letras = []
        letras.append(request.form.get("one"))
        letras.append(request.form.get("two"))
        letras.append(request.form.get("three"))
        letras.append(request.form.get("four"))
        letras.append(request.form.get("five"))
        if d.check(listToString(letras)) == False:
            flash('Invalid Word!')
            check[0] = "."
            return redirect(url_for('index4'))
        if check[0] == "":
            lista.append(letras)
        certo = 0
        for i in range(0,5) :
            if lista[3][i].lower() == session["word1"][i].lower():
                certo = certo + 1
        if certo == 5:
            return redirect(url_for("index7"))
        print(letras)
        session["1"] = lista
        return redirect(url_for("index5") )

@app.route("/index5", methods = ["GET", "POST"])
def index5():
    if request.method == "GET":
        return render_template("index5.html", lista=session["1"], word=session["word1"],certo=session["2"])
    else:
        check[0] = ""
        word = pick_random_word()
        letras = []
        letras.append(request.form.get("one"))
        letras.append(request.form.get("two"))
        letras.append(request.form.get("three"))
        letras.append(request.form.get("four"))
        letras.append(request.form.get("five"))
        if d.check(listToString(letras)) == False:
            flash('Invalid Word!')
            check[0] = "."
            return redirect(url_for('index5'))
        if check[0] == "":
            lista.append(letras)
        certo = 0
        for i in range(0,5) :
            if lista[4][i].lower() == session["word1"][i].lower():
                certo = certo + 1
        if certo == 5:
            return redirect(url_for("index7"))
        print(letras)
        session["1"] = lista
        print(session["1"])
        return redirect(url_for("index8") )
    
@app.route("/index7", methods = ["GET", "POST"])
def index7():
    if request.method == "GET":
        return render_template("index7.html")
    
@app.route("/index8", methods = ["GET", "POST"])
def index8():
    if request.method == "GET":
        print (session["word1"])
        return render_template("index8.html", word=session["word1"])
    
    
    


