from flask import Flask, render_template, request, session
import requests
import time

app = Flask(__name__)
app.secret_key = "my_key"

# templates
@app.route('/<int:n>', methods=["GET", "POST"])
def index(n):
	if request.method == 'POST':
		nm = request.form["nm"]
		return render_template("index.html", 
		n=nm, items = ['a','b','c'])
	else:	
		return render_template("index.html", 
		n=n, items = ['a','b','c'])


@app.route('/', methods=["GET", "POST"])
def page():
	if request.method == 'POST':
		data = request.form["number"]
		session["data"] = data 
		return data
	else:
		return render_template("number.html")
    
@app.route("/session")
def ses():
	return "Data="+str(session.get("data"))


@app.route('/counter/')
def counter():
	if "visitors" in session:
		session["visitors"] = session.get("visitors") + 1
		return "Users:"+ str(session.get("visitors"))
	else: 
		session["visitors"] = 1
		return "First USER!!!!"

@app.route('/del/')
def delete():
	session["visitors"] = 0
	return "Users = 0" 


if __name__ == '__main__':
	app.run(debug=True)
