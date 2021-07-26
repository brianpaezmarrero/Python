from flask import Flask,render_template, redirect, request
from friends import Friend

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route('/')
def index():
    return render_template("index.html",all_friends = Friend.get_all())


@app.route('/friend/new')
def new_friend():
    return render_template("friend.html")

@app.route("/friend/add", methods = ["POST"])
def add_friend():
    # print(request.form)
    Friend.create(request.form)

    return redirect("/")

@app.route('/friend/<int:friend_id>')
def display_friend(friend_id):
    return render_template("the_friend.html", the_friend = Friend.get_one({"id": friend_id}) )

if __name__ == '__main__':
    app.run(debug=True)