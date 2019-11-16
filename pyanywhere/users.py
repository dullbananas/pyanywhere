from . import API_ROOT
import os
import getpass


class User:
	__slots__ = (
		'name', 'token', 'endpoint',
	)
	
	def __init__(self, name, token=None):
		self.name = name
		self.token = token
		self.endpoint = f'{API_ROOT}/user/{name}'


def get_current_user():
	name = getpass.getuser()
	token = os.getenv('API_TOKEN', None)
	return User(name=name, token=token)
