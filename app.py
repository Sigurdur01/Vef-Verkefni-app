#Sigurður Ingi Brynjarsson
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return '<h1>Hello World!</h1> <a href='/'> Home </a> <a href='/sida2'> Sida2 </a> <a href='/sida3'> Sida3 </a>'

@app.route("/sida2")
def sida2():
    return '<h1>Hello World!</h1> <a href='/'> Home </a> <a href='/sida2'> Sida2 </a> <a href='/sida3'> Sida3 </a>'
@app.route("/sida3")
def sida3():
    return '<h1>Hello World!</h1> <a href='/'> Home </a> <a href='/sida2'> Sida2 </a> <a href='/sida3'> Sida3 </a>'

if __name__== '__main__':
    app.run(debug=True)
