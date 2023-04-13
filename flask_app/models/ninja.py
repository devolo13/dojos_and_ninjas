# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# model the class after the friend table from our database


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # Method for adding a new ninja to the database
    @classmethod
    def save(cls, data):
        query = 'INSERT into ninjas ( dojo_id, first_name, last_name, age, created_at, updated_at) values ( %(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW() );'
        return connectToMySQL(DATABASE).query_db(query, data)
