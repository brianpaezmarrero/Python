from types import SimpleNamespace
from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."

@app.route("/")
def index():

    session['count'] = 1

    if 'count' in session:
        print('working')
    for session['count'] in session:
        session['count'] =+ 1
        return session['count']


    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug = True)