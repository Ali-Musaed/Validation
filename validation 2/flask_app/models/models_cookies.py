from flask_app.config.mysqlconnections import connectToMySQL
from flask import flash
import re

db = 'cookie' 

class Cookie:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.first_name = db_data['cookie_type']
        self.last_name = db_data['num_of_boxes']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM cookies
                """
        results = connectToMySQL(db).query_db(query)
        cookies = []
        for cookie in results:
            cookies.append(cookie)
        return results
    @classmethod
    def get_one(cls, data):
        query = f"SELECT * FROM cookies where id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return (results[0])
    @classmethod
    def save(cls, data):
        query = f"INSERT INTO cookies (first_name, cookie_type, num_of_boxes, created_at, updated_at) VALUES (%(first_name)s,%(cookie_type)s, %(num_of_boxes)s, NOW(), NOW());"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def delete(cls, data, cookie_id):
        query = f"delete FROM cookies where id = {cookie_id};"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def update(cls, form_data, cookie_id):
        query = f"UPDATE cookies SET first_name = %(first_name)s, cookie_type = %(cookie_type)s, num_of_boxes = %(num_of_boxes)s WHERE id = {cookie_id};"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        return connectToMySQL(db).query_db(query, form_data)
        # Create an empty list to append our instances of friends
    @staticmethod
    def validate_order(cookie):
        is_valid = True # we assume this is true
        if len(cookie["first_name"]) == 0:
            flash("First name must be at least 1 characters.")
            is_valid = False
        if len(cookie['cookie_type']) < 3:
            flash("cookie type must be at least 4 characters.")
            is_valid = False
        if int(cookie['num_of_boxes']) <= 0:
            flash("Invalid number of boxes!")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_cookie(order):
        is_valid = True # we assume this is true
        if len(order["first_name"]) == 0:
            flash("First name must be at least 1 characters.")
            is_valid = False
        if len(order['cookie_type']) < 3:
            flash("cookie type must be at least 4 characters.")
            is_valid = False
        if int(order['num_of_boxes']) <= 0:
            flash("Invalid number of boxes!")
            is_valid = False
        return is_valid