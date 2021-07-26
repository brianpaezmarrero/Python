from flask import render_template,request,redirect,session, flash
from flask_bcrypt import Bcrypt  

from flask_app import app
from ..models.user import User

bcrypt = Bcrypt(app)


# CREATE
@app.route('/')
def index():
    if "uuid"  in session:
        return redirect('/show/all')
    
    return render_template("index.html")

@app.route("/user/create", methods = ["POST"])
def new_user():

    if not User.register_validate(request.form):
        return redirect('/')

    
    hash_brown = bcrypt.generate_password_hash(request.form['password'])
    data ={
        **request.form,
        'password': hash_brown
    }

    user_id = User.create(data)

    session['uuid'] = user_id

    return redirect('/show/all')




# GET_ALL
@app.route('/show/all')
def show_all():
    if "uuid" not in session:
        flash("MUST LOG IN")
        return redirect('/')

    return render_template('show_all.html', all_users = User.get_all(), user = User.get_by_id({'id': session['uuid']}))


@app.route("/user/login", methods = ["POST"])
def login():

    if not User.login_validate(request.form):
        return redirect('/')

    user = User.get_by_email({'email': request.form['email']})

    session['uuid'] = user.id
    return redirect('/show/all')


@app.route("/user/logout")
def logout():
    session.clear()

    return redirect("/")




# GET_ONE
@app.route('/user/<int:user_id>/show')
def show_one(user_id):

    return render_template('show_one.html', user = User.get_one({'id': user_id}))






# DESTROY
@app.route('/user/<int:user_id>/destroy')
def destroy_user(user_id):
    return redirect('/show/all', User.destroy({'id': user_id}))




# UPDATE
@app.route('/user/<int:user_id>/edit')
def edit_user(user_id):
    return render_template('edit_user.html', user = User.get_one({'id': user_id}))

@app.route('/user/<int:user_id>/update', methods = ["POST"])
def update_user(user_id):
    
    new_dict = {
        **request.form,
        "id": user_id
    }

    User.update(new_dict)

    return redirect('/show/all')


