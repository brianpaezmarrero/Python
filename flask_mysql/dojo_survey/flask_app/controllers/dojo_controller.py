from ..models.dojos import Dojos
from flask_app import app
from flask import render_template, redirect, request,session, url_for


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/create', methods=['POST'])
def create_survey():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not Dojos.validate_dojos(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    Dojos.create(request.form)
    return redirect("/show")


@app.route('/show')
def show_result():

    return render_template('show.html', all_dojos = Dojos.get_all())

