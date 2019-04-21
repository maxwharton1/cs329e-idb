from flask import Flask, render_template
import subprocess
from create_db import app, db, Shark, Investment, create_sharks, create_deals
from sqlalchemy.inspection import inspect


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sharks')
def sharks():
    books = db.session.query(Shark).all()
    return render_template('sharks.html', books = books)

@app.route('/deals')
def deals():
    books = db.session.query(Investment).all()
    return render_template('deals.html', books = books)


@app.route('/shark/<shark>')
def thisShark(shark):

    shark = db.session.query(Shark).filter(Shark.url == shark)
    return render_template('thisShark.html', shark = shark)

@app.route('/company/<thisComp>')
def thisComp(thisComp):

    deal = db.session.query(Investment).filter(Investment.url == thisComp)
    return render_template('thisComp.html', deal = deal)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/test')
def test():
    p = subprocess.Popen(["coverage", "run", "--branch", "test.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
    out, err = p.communicate()
    output=err+out
    output = output.decode("utf-8") #convert from byte type to string type

    return render_template('test.html', output = "<br/>".join(output.split("\n")))

@app.route('/search/<s>')
def search():
    #I would really really like to see if hte substring matches any
    #substring in the ql characteristics.
    found = []
    sharkT = inspect(Shark)
    investT = inspect(Investment)

    #searches for the substring in every instance var of Shark
    for column in sharkT.c:
        found.append(Shark.query.filter(Shark.column.contains(s)))

    #searches for the substring in eveyr instance var of Investment
    for column in investT.c:
        found.appned(Investment.query.filter(Inestment.column.contains(s)))

    return render_template('search.html', var = found)

if __name__ == "__main__":

    app.run(debug = True)
