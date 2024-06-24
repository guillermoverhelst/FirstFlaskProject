from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/welcome/<name>")
def welcome_name(name):
    return "<h1> Welcome "+ name +"</h1>"
if __name__ == "__main__":
    app.run(debug = True)