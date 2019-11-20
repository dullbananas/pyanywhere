from . import API_ROOT
from .consoles import Console
from .exceptions import APIError
import os
import getpass
import requests


class User:
	'''The User class represents a PythonAnywhere user. It is the central object
	because it has to be used in order to access anything else. When running this
	module from PythonAnywhere, the :func:`pyanywhere.users.get_current_user` function can
	be used to automatically generate this object.
	
	:param name: The username.
	
	:param token: The API token that is associated with the user.
	'''
	
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
		'''This method gets the consoles that are running on the user.
		
		:return: A geterator yielding :class:`pyanywhere.consoles.Console`
		         objects.
		'''
		return self._list_consoles('/consoles/')
	
	def get_shared_consoles(self):
		'''A variant of :meth:`get_consoles` that yields consoles shared with the
		user.
		'''
		return self._list_consoles('/consoles/shared_with_you/')
	
	def start_console(self, exec_name, args, working_dir):
		'''This method starts a new console.
		
		:param exec_name: The name of the executable used for the console. For
		                  example, you can set this to ``'bash'`` to start a Bash
		                  console.
		
		:param args: The command line arguments passed to ``exec_name``. This
		             must be a string.
		
		:param working_dir: The initial working directory of the console.
		
		:return: A :class:`pyanywhere.consoles.Console` object.
		'''
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
	'''This function can be used to return a :class:`pyanywhere.users.User` object if this
	module is running on PythonAnyhwere. It gets your username by getting your
	Linux username, and it gets your API token from the ``API_TOKEN`` environment
	variable.
	'''
	name = getpass.getuser()
	token = os.getenv('API_TOKEN', None)
	return User(name=name, token=token)
