class Console:
	'''Represents a console. Can be retrieved from the
	:class:`pyanywhere.users.User` class.
	'''
	
	__slots__ = (
		'id', 'owner', 'executable', 'arguments', 'working_dir', 'name', 'url',
		'frame_url', 'endpoint',
	)
	
	def __init__(self, id, owner, executable, arguments, working_dir, name, url, frame_url):
		self.id = id
		self.owner = owner
		self.executable = executable
		self.arguments = arguments
		self.working_dir = working_dir
		self.name = name
		self.url = url
		self.frame_url = frame_url
		self.endpoint = f'{owner.endpoint}/consoles/{id}'
	
	def get_latest_output(self, replace_newlines=False):
		'''Gets the latest output from the console. This will contain CRLF
		(Windows, ``\\r\\n``) newlines. According to the API's help page, this
		will return approximately 500 characters.
		
		:param replace_newlines: Replace ``\\r\\n`` with ``\\n``.
		
		:return: A string
		'''
		output = self.owner._request('get', f'/consoles/{self.id}/get_latest_output/')['output']
		if replace_newlines:
			output = output.replace('\r\n', '\n')
		return output
	
	def kill(self):
		'''Kills the console.'''
		self.owner._request('delete', f'/consoles/{self.id}/')
	
	def send_input(self, data):
		'''Sends a string to the console's stdin (types into the console).
		
		:param data: The string to send to the console.
		'''
		self.owner._request('post', f'/consoles/{self.id}/send_input/', data={
			'input': data,
		})
