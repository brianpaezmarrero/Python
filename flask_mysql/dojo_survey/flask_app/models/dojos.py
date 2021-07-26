from ..config.mysqlconnection import connectToMySQL

from flask import flash
# Other Burger methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger

class Dojos:
    def __init__(self, data):
        self.id = data['id'],
        self.name = data['name'],
        self.location = data['location'],
        self.language = data['language'],
        self.comment = data['comment'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_dojos(post_data):
        #post_data is the data from request.form
        #it is a bool
        is_valid = True # we start with assuming the data is valid

        # we check the statments to check the data 
        # if the data isn't valid, we set is_valid = False

#       the data we get from the form is all a string
        if len(post_data['name']) < 3:
            # flash messages exist for just one HTTP req/res cycle
            flash('Dojo Name must be bigger at least 3 char')
            is_valid = False

        if len(post_data['location']) == len('N/A'):
            flash('Select an Option')
            is_valid = False

        if len(post_data['language']) == len('N/A'):
            flash('Select an Option')
            is_valid = False

        if len(post_data['comment']) < 1:
            flash('Comments should not be empty')
            is_valid = False


        return is_valid

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO dojos (name, location, language, comment)
        VALUES (%(name)s,%(location)s,%(language)s,%(comment)s)
        """
        dojo_id = connectToMySQL('dojo_survey').query_db(query,data)

        return dojo_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_survey').query_db(query)

        dojos = []

        for row in results:
            dojos.append(row)

        return dojos


    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM dojos
        WHERE id = %(id)s
        """
        results = connectToMySQL('dojo_survey').query_db(query, data)

        return cls(results[0])


    