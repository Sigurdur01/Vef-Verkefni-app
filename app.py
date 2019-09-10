#Sigurður Ingi Brynjarsson
from flask import Flask
from sys import argv
app = Flask(__name__)
@app.route("/")
def index():
    return '<li><a href='/'> 'Home' </a> </li><li><a href='/sida2'> 'Sida2' </a> </li><li><a href='/sida3'> 'Sida3' </a></li>'

@app.route("/sida2")
def sida2():
    return '<li><a href='/'> 'Home' </a> </li><li><a href='/sida2'> 'Sida2' </a> </li><li><a href='/sida3'> 'Sida3' </a></li>'

@app.route("/sida3")
def sida3():
    return '<li><a href='/'> 'Home' </a> </li><li><a href='/sida2'> 'Sida2' </a> </li><li><a href='/sida3'> 'Sida3' </a></li>'


if (__name__) == '__main__':
    app.run(debug=True)