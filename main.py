from flask import Flask, render_template
from create_db import app, db, Book, create_books
from format import toURL, fromURL

app = Flask(__name__)

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
    sharkName = fromURL(shark)
    #filter beneath this statement is a little sketchy
    #books = db.session.query(Deal).filter(shark ==  ds.lower() for ds in Deal.sharks)
    deals = db.session.query(Deal).filter(sharkName in Deals.sharks) #checks the deals that have our current shark in the array of names
    shark = db.session.query(Shark).filter(Shark.name == sharkName)
    return render_template('thisShark.html', deals = deals, shark = shark)

@app.route('/company/<thisComp>')
def thisComp(thisComp):
    thisComp = fromURL(thisComp)
    deals = db.session.query(Deal).filter(Deal.name == thisComp)
    return render_template('thisComp.html', deals = deals)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":

    app.run(debug = True)
