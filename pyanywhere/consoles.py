class Console:
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
		output = self.owner._request('get', f'/consoles/{self.id}/get_latest_output/')['output']
		if replace_newlines:
			output = output.replace('\r\n', '\n')
		return output
	
	def kill(self):
		self.owner._request('delete', f'/consoles/{self.id}/')
	
	def send_input(self, data):
		self.owner._request('post', f'/consoles/{self.id}/send_input/', data={
			'input': data,
		})
