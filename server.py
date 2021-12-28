from user import User
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users')
def users():
    return render_template("read_all.html", users = User.get_all())

@app.route('/users/new')
def new():
    return render_template("create.html")

@app.route('/users/create',methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')

# @app.route('/users/new', methods=["POST"])
# def create_user():
#     data = {
#         "id": request.form["id"],
#         "fname": request.form["fname"],
#         "lname" : request.form["lname"],
#         "email" : request.form["email"],
#         "created_at": request.form["created_at"]
#     }
#     User.save(data)
#     return render_template("create.html")

if __name__ == '__main__':
    app.run(debug=True)