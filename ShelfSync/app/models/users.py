"""
Define data models for users
"""

import json

class Users:

	"""
	Returns Json representation of user data

	...

	"""

	def __init__(self, id, name, email, phone, username, password):

		self.id = id
		self.name = name
		self.email = email
		self.phone = phone
		self.username = username
		self.password = password


	def to_json(self):
		return {

			'id': self.id
			'name': self.name,
			'email': self.email,
			'phone': self.phone,
			'username': self.username,
			'password': self.password
		}



class Employee(Users):
	
	""""Returns json representation of Employee data"""

	def __init__(self, id, name, email, phone, username, password, position, isAdmin):
		super().__init__(self, id, name, email, phone, username, password):
		self.position = position
		self.isAdmin = isAdmin


	def to_json(self):
		data = super().to_json()
		data["position"] = self.position
		data["isAdmin"] = self.isAdmin
		return data



class Patrons(Users):
	
	"""Returns string representaion of patron's data"""

	def __init__(self, id, name, email, phone, username, password, address):
		super()__init__(self, id, name, email, phone, username, password)
		self.address = address


	def to_json(self):
		data = super.to_json()
		data["address"] = self.address