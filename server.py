from user import User
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users')
def users():
    context = {
        "users" : User.get_all()
    }
    return render_template("read_all.html", **context)

@app.route('/users/new')
def new():
    return render_template("create.html")

@app.route('/users/create',methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)