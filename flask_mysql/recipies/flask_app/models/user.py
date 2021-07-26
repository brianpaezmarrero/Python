from ..config.mysqlconnection import connectToMySQL

from flask import flash

import re

from flask_bcrypt import Bcrypt
from flask_app import app

bcrypt = Bcrypt(app)



class User:
    schema = 'recipes'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']




# CREATE
    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        user_id = connectToMySQL(cls.schema).query_db(query, data)

        return user_id





    @staticmethod
    def register_validate(post_data):
        

        is_valid = True

        if len(post_data['first_name']) < 2:
            flash("First Name must be grater than 2 char")
            is_valid = False

        if len(post_data['last_name']) < 2:
            flash("Last Name must be grater than 2 char")
            is_valid = False

        if len(post_data['password']) < 8:
            flash("Password must be greater than 8 char")
            is_valid = False
        elif post_data['password'] != post_data['confirm_password']:
            flash("Password and confirm password must match")
            is_valid = False


        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if not EMAIL_REGEX.match(post_data['email']):
            flash("Invalid email address!")
            is_valid = False
        elif User.get_by_email({'email': post_data['email']}):
            flash("Email is already in use")
            is_valid = False



        return is_valid


    @staticmethod
    def login_validate(post_data):
        user = User.get_by_email({'email': post_data['email']})

        if not user:
            flash('Invalid Credentials')
            return False

        if not bcrypt.check_password_hash(user.password, post_data['password']):
            flash('Invalid Credentials')
            return False

        return True



# GET_ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.schema).query_db(query)
        
        users = []

        for row in results:
            users.append(row)

        return users



# GET_ONE
    @classmethod
    def get_one(cls , data):
        query = """
        SELECT * FROM users
        WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.schema).query_db(query, data)

        return cls(results[0])



# GET_BY_EMAIL
    @classmethod
    def get_by_email(cls , data):
        query = """
        SELECT * FROM users
        WHERE email = %(email)s;
        """
        results = connectToMySQL(cls.schema).query_db(query, data)

        if len(results) < 1:
            return False

        return cls(results[0])




# GET_BY_ID
    @classmethod
    def get_by_id(cls , data):
        query = """
        SELECT * FROM users
        WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.schema).query_db(query, data)

        return cls(results[0])


# UPDATE
    @classmethod
    def update(cls, data):
        query = """
        UPDATE users SET first_name = %(first_name)s, first_name = %(last_name)s, first_name = %(email)s, first_name = %(password)s,
        WHERE id = %(id)s;
        """

        return connectToMySQL(cls.schema).query_db(query, data)



# DESTROY
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"

        return connectToMySQL(cls.schema).query_db(query, data)