from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    Title = db.Column(db.String(200), nullable = False)
    Description = db.Column(db.String(500), nullable = False)
    time = db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.Title}"

@app.route("/",methods=['GET','POST'])
def add():
    if request.method == 'POST':
        todo_title = request.form['title']
        todo_desc = request.form['desc']
        data = Todo(Title=todo_title,Description = todo_desc)
        db.session.add(data)
        db.session.commit()
        db.session.close()
    alltodo = Todo.query.all()
    return render_template("index.html",alltodo = alltodo)

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno = sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>", methods=['GET','POST'])
def update(sno):
    if request.method == "POST":
        todo_title = request.form['title']
        todo_desc = request.form['desc']
        data = Todo.query.filter_by(sno = sno).first()
        data.Title = todo_title
        data.Description = todo_desc
        db.session.add(data)
        db.session.commit()
        return redirect("/")
    todo = Todo.query.filter_by(sno = sno).first()
    return render_template("update.html", todo = todo)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True)