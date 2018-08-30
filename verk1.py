#Sigurður Ingi Brynjarsson

from sys import argv
from bottle import *
bottle.debug(True)

@route('/')
def index():
    return"""
    <h1>Verkefni 1</h1>
    <p><a href='/about'>About page</a></p>
    <p><a href='/bio'>Bio page</a></p>
    <p><a href='/future'>Future page</a></p>
    """


@route("/about")
def jobbi():
    return "about page here"

@route("/bio")
def jobbi():
    return "bio page here"

@route("/future")
def jobbi():
    return "future page here"


bottle.run(host='0.0.0.0', port=argv[1])
