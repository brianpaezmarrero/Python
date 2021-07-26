from flask import render_template, redirect, request
from flask_app import app
from ..models.dojos import Dojos
from ..models.ninjas import Ninjas

@app.route('/ninja/show')
def show_ninjas():
    return render_template('ninja/ninjas.html',all_ninjas = Ninjas.get_all())

@app.route('/ninja/new')
def new_ninja():
    return render_template("ninja/new_ninja.html", all_dojos = Dojos.get_all())

@app.route('/ninja/create', methods = ['POST'])
def create_ninja():

    Ninjas.create(request.form)
    return redirect('/')
