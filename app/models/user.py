"""

User model

"""
from flask import jsonify

class User:

    def __init__(self, name):
        self.name = name


    def user_data(self):
        return jsonify({"name": self.name})