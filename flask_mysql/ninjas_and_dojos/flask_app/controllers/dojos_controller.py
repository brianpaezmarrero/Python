from flask import render_template, redirect, request
from flask_app import app
from ..models.dojos import Dojos

@app.route('/')
def index():
    return render_template('index.html', all_dojos = Dojos.get_all())

@app.route('/dojo/new')
def new_dojo():
    return render_template('dojo/new_dojo.html')

@app.route('/dojo/create', methods = ['POST'])
def created_dojo():

    Dojos.create(request.form)


    return redirect('/')

@app.route('/dojo/<int:dojo_id>')
def show_dojo(dojo_id):

    return render_template('dojo/show_dojo.html', dojo = Dojos.get_one({'id': dojo_id}))

@app.route('/dojo/<int:dojo_id>/edit')
def edit_dojo(dojo_id):

    return render_template('dojo/edit_dojo.html', dojo = Dojos.get_one({'id': dojo_id})) 

@app.route('/dojo/<int:dojo_id>/update', methods = ["POST"])
def update_dojo(dojo_id):

    new_dict = {
        **request.form,
        "id": dojo_id
    }

    Dojos.update(new_dict)

    return redirect('/')

@app.route("/dojo/<int:dojo_id>/destroy")
def destroy_dojo(dojo_id):

    Dojos.destroy({'id': dojo_id})
    
    return redirect('/')