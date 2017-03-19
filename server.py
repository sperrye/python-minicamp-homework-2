from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def land():
    return render_template('home.html')

@app.route('/birthday')
def bday():
    return 'August 23, 1987'

@app.route('/greeting/<name>')
def greet(name):
    return 'Hello %s' % name

@app.route('/add/<int:n1>/<int:n2>')
def add(n1,n2):
    result = n1+n2
    return str(result)

@app.route('/multiply/<int:n1>/<int:n2>')
def multiply(n1, n2):
    result = n1 * n2
    return str(result)

@app.route('/subtract/<int:n1>/<int:n2>')
def subtract(n1, n2):
    result = n1 - n2
    return str(result)

@app.route('/favoritefoods')
def foods():
    list = ['icecream', 'salad', 'coffee']
    return jsonify(list)
