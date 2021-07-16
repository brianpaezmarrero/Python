from typing import Iterable
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:num>/<color>')
def add_box(num):
    return render_template("box.html",num=num)

if __name__=="__main__":
    app.run(debug=True)