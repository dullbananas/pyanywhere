from . import API_ROOT
from .consoles import Console
from .exceptions import APIError
import os
import getpass
import requests


class User:
	__slots__ = (
		'name', 'token', 'endpoint',
	)
	
	def __init__(self, name, token=None):
		self.name = name
		self.token = token
		self.endpoint = f'{API_ROOT}/user/{name}'
	
	def _request(self, method, url, **kwargs):
		response = getattr(requests, method)(
			self.endpoint + url,
			headers={'Authorization': f'Token {self.token}'},
			**kwargs,
		).json()
		if 'detail' in response:
			raise APIError(response['detail'])
		return response
	
	def _list_consoles(self, endpoint):
		response = self._request('get', '/consoles/')
		for i in response:
			yield Console(
				id=i['id'],
				owner=self,
				executable=i['executable'],
				arguments=i['arguments'],
				working_dir=i['working_directory'],
				name=i['name'],
				url=i['console_url'],
				frame_url=i['console_frame_url'],
			)
	
	def get_consoles(self):
		return self._list_consoles('/consoles/')
	
	def get_shared_consoles(self):
		return self._list_consoles('/consoles/shared_with_you/')
	
	def start_console(self, exec_name, args, working_dir):
		response = self._request('post', '/consoles/', data={
			'executable': exec_name,
			'arguments': args,
			'working_directory': working_dir,
		})
		return Console(
			id=response['id'],
			owner=self,
			executable=exec_name,
			arguments=args,
			working_dir=working_dir,
			name=response['name'],
			url=response['console_url'],
			frame_url=response['console_frame_url'],
		)


def get_current_user():
	name = getpass.getuser()
	token = os.getenv('API_TOKEN', None)
	return User(name=name, token=token)
