from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."

@app.route("/")
def index():
    session['counter'] = request.form['count']
    if 'counter' in session:
        print(session['counter'])
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug = True)