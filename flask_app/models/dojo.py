# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# model the class after the friend table from our database


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # Method for getting all dojos in the database. Returns a list of dojo objects
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    # Method to get a single dojo. Returns dojo object
    @classmethod
    def get_by_id(cls, id):
        data = {'id': id}
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = cls(results[0])
        return user

    # Method for adding a new dojo to the database
    @classmethod
    def save(cls, data):
        query = 'INSERT into dojos ( name, created_at, updated_at) values (%(name)s, NOW(), NOW() );'
        return connectToMySQL(DATABASE).query_db(query, data)

    # Method for getting all ninjas in a dojo. Returns list of ninja objects
    @classmethod
    def get_ninjas_by_dojo(cls, data):
        query = 'SELECT first_name, last_name, age, name FROM ninjas JOIN dojos on dojos.id = ninjas.dojo_id WHERE dojo_id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        ninjas = []
        for person in results:
            ninjas.append(person)
        return ninjas
