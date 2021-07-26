# import the function that will return an instance of a connection
from mysqlconection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL("first_flask").query_db(query)

        all_friends = [""]

        for row in results:
            all_friends.append(cls(row))

        return all_friends

    @classmethod
    def get_one(cls, data):

        query = "SELECT * FROM frinds WHERE id = %(id)s;"
        results = connectToMySQL("first_flask").query_db(query, data)

        return cls(results[0])

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());
    """
        friend_id = connectToMySQL("first_flask").query_db(query, data)

        return friend_id

