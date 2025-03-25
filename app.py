from flask import Flask

#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask application"

@app.route("/index")
def index():
    return "Welcome to the index route"

if __name__=="__main__":
    app.run(debug=True)
