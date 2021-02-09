from flask import Flask, render_template #Importing a file
app = Flask(__name__) #Create an instance of this class

@app.route('/') # the route() decorator to tell Flask what URL should trigger our function.
def index():
	return render_template("index.html")
	#or simply return a String

@app.route('/about') # the route() decorator to tell Flask what URL should trigger our function.
def about():
	return render_template("about.html")
	#or simply return a String

@app.route('/contact') # the route() decorator to tell Flask what URL should trigger our function.
def contact():
	return render_template("contact.html")
#To Run This go to file dir i.e snap/ProgramPy/flask WebApps$ FLASK_APP=hello.py flask run
#To turn on debug mode : export FLASK_ENV=development
