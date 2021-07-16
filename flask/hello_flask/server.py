from typing_extensions import IntVar
from flask import Flask 

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'

@app.route('/<string:say>/<string:name>')
def name(say,name):
    return f"{say} {name}"

@app.route('/repeat/<string:hello>/<int:num>')
def repeat(hello,num):
    return f"{hello * num}"


if __name__=='__main__':
    app.run(debug=True)