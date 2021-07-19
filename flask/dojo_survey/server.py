from flask import Flask, render_template, redirect, request,session, url_for

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ["POST"])
def results():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['fav_lng'] = request.form['fav_lng']
    session ['info'] = request.form['info']
    if 'name' in session:
        print(session['name'])
    if 'loction' in session:
        print(session['location'])
    if 'fav_lng' in session:
        print(session['fav_lng'])
    if 'info' in session:
        print(session['info'])
    return redirect(url_for('show_result'))

@app.route('/show')
def show_result():
    print(request.form)
    return render_template('show.html')



if __name__ == '__main__':
    app.run(debug=True)