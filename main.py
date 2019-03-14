from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): #this should route to the landing page
    return render_template('index.html')

@app.route('/sharks')
def sharks():
    return render_template('sharks.html')

@app.route('/deals')
def deals():
    return render_template('deals.html')


@app.route('/shark/<shark>')
def thisShark(shark):
    return render_template('thisShark.html')

@app.route('/company/<thisComp>')
def thisComp(thisComp):
    return render_template('thisComp.html')

'''
@app.route('/oleary')
def oleary(shark):
    return render_template("kevin_oleary.html")

@app.route('/cuban') #why don't we do it by
def cuban(shark):
    return render_template("mark_cuban.html")

@app.route('/daymond_john')
def john():#
    return render_template('john.html')


@app.route('/herjavec')
def herjavec(compName):
    return render_template('robert_herjavec.html')

'''

if __name__ == "__main__":

    app.run(debug = True)
