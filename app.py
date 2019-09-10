  
#Sigurður Ingi Brynjarsson
from flask import Flask,render_template,redirect
from sys import argv
app = Flask(__name__)
hrefs = {
    "href main":"/",
    "href sida2":"/sidur/2",
    "href sida3":"/sidur/3"
}
linktext = {
    "Hlekur1":"Heim",
    "Hlekur2":"Sida2",
    "Hlekur3":"Sida3"
}
contents = {
    "content":"Hello Universe",
    "Hlekur1":linktext["Heim"],
    "Hlekur2":linktext["Hlekur2"],
    "Hlekur3":linktext["Hlekur3"],
    "href1":hrefs["href main"],
    "href2":hrefs["href sida2"],
    "href3":hrefs["href sida3"]
}
sida2contents = {
    "content":"detta er Sida 2",
    "Hlekur1":linktext["Heim"],
    "Hlekur2":linktext["Hlekur2"],
    "Hlekur3":linktext["Hlekur3"],
    "href1":hrefs["href main"],
    "href2":hrefs["href sida2"],
    "href3":hrefs["href sida3"]
}
sida3contents = {
    "content":"detta er Sida 3",
    "Hlekur1":linktext["Heim"],
    "Hlekur2":linktext["Hlekur2"],
    "Hlekur3":linktext["Hlekur3"],
    "href1":hrefs["href main"],
    "href2":hrefs["href sida2"],
    "href3":hrefs["href sida3"]
}
@app.route("/")
def index():
    return render_template('head.html', cnt=contents)
@app.route("/sidur/<int:sidunumber>", methods=['Get'])
def sida(sidunumber):
    if sidunumber == 1:
        return redirect("/")
    elif sidunumber == 2:
        return render_template('head.html', cnt=sidu2contents)
    elif sidunumber == 3:
        return render_template('head.html', cnt=sidu3contents)
if (__name__) == '__main__':
    app.run(debug=True)