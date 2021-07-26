from ..config.mysqlconnection import connectToMySQL

from ..models import dojos


class Ninjas:
    def __init__(self, data):
        self.id = data['id']
        # self.dojo_id = data['dojo_id']
        if 'dojo_id' in data:
            self.dojo = dojos.Dojos.get_one({"id": data['dojo_id']})
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """INSERT INTO ninjas (dojo_id, first_name, last_name, age)
        VALUES(%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);
        """
        ninja_id = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        return ninja_id
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)

        ninjas = []

        for row in results:
            ninjas.append(cls(row))

        return ninjas
        

    # @classmethod
    # def get_one(cls, data):
    #     query = "SELECT * FROM ninjas WHERE id = %(id)s;"

    #     results = connectToMySQL('dojos_and_ninjas').query_db(query, data)

    #     return cls(results[0])


    # @classmethod
    # def update(cls, data):
    #     query = """
    #     UPDATE ninjas SET name = %(name)s
    #     WHERE id = %(id)s; 
    #     """
    #     return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    # @classmethod
    # def destroy(cls, data):
    #     query = "DELETE FROM ninjas WHERE id = %(id)s;"

    #     return connectToMySQL('dojos_and_ninjas').query_db(query, data)