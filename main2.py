from flask import Flask, render_template
from create_db import app, db, Book, create_books

app = Flask(__name__)

@app.route('/')
def index(): #this should route to the landing page
    return render_template('index.html')

@app.route('/sharks')
def sharks():
    books = db.session.query(Book).all()
    return render_template('sharks.html', books = books)

@app.route('/deals')
def deals():
    return render_template('deals.html')


@app.route('/shark/<shark>')
def thisShark(shark):
    return render_template('thisShark.html')

@app.route('/company/<thisComp>')
def thisComp(thisComp):
    return render_template('thisComp.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":

    app.run(debug = True)
