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

pg2contents = {
                "content":"Þetta er Sida 2",
		"Hlekur1":linktext["Heim"],
                "Hlekur2":linktext["Hlekur2"],
                "Hlekur3":linktext["Hlekur3"],
		"href1":hrefs["href main"],
                "href2":hrefs["href sida2"],
                "href3":hrefs["href sida3"]
               }

pg3contents = {
                "content":"This is page3",
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


@app.route("/sidur/<int:pgnumber>", methods=['Get'])
def page(pgnumber):
    if pgnumber == 1:
        return redirect("/")
    elif pgnumber == 2:
        return render_template('head.html', cnt=pg2contents)
    elif pgnumber == 3:
        return render_template('head.html', cnt=pg3contents)

if (__name__) == '__main__':
    app.run(debug=True)
