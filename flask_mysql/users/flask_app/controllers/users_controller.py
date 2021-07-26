from flask import render_template,redirect,request
from flask_app import app 
from flask_app.models.users import Users

# display all users
@app.route('/')
def index():
    return render_template("index.html", all_users = Users.get_all())
    
# page to create a new users
@app.route("/user/new")
def new_user():
    return render_template('new_user.html')

# post the created user
@app.route("/user/create", methods = ["POST"])
def created_user():
    
    Users.create(request.form)

    return redirect('/')

# display one user
@app.route('/user/<int:user_id>')
def one_user(user_id):
    return render_template('user.html', user = Users.get_one({'id': user_id}))
    
# display a page to update
@app.route('/user/<int:user_id>/edit')
def edit_user_form(user_id):
    return render_template("edit_user.html", user = Users.get_one({'id': user_id}))

# update the user selected
@app.route('/user/<int:user_id>/update', methods = ["POST"])
def update_dog(user_id):
    new_dict = {
        **request.form,
        "id": user_id
    }
    Users.update(new_dict)

    return redirect('/')

# deletes a user
@app.route('/user/<int:user_id>/delete')
def delete_user(user_id):

    Users.delete({"id": user_id})

    return redirect('/')
