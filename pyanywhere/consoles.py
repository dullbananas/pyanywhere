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
