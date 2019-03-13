from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sharks')
def sharks():
    return render_template('sharks.html')


@app.route('/companies')
def companies():
    return render_template('companies.html')


@app.route('/companies/<compName>')
def thisCompany(compName):
    return render_template('company.html', compName)


@app.route('/<shark>')
def thisShark(shark):
    return render_template("shark.html", shark)



if __name__ == "__main__":
    app.run(debug = True)
