from ..config.mysqlconnection import connectToMySQL

from flask_app.models import ninjas 

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create(cls, data):
        query = """INSERT INTO dojos (name)
        VALUES(%(name)s);
        """
        dojo_id = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        return dojo_id
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)

        dojos = []

        for row in results:
            dojos.append(cls(row))

        return results
        

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"

        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        
        
        dojo = cls(results[0])


        for row in results:
            row_data ={
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }

            dojo.ninjas.append(ninjas.Ninjas(row_data))

        return dojo


    @classmethod
    def update(cls, data):
        query = """
        UPDATE dojos SET name = %(name)s
        WHERE id = %(id)s; 
        """
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"

        return connectToMySQL('dojos_and_ninjas').query_db(query, data)