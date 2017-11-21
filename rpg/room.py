class Room():

	def __init__(self):
		self.name 			  = None
		self.description  = None
		self.linked_rooms = {}
		self.character 	  = None
		self.item 				= None

	def __init__(self, room_name):
		self.name 			  = room_name
		self.description  = None
		self.linked_rooms = {}
		self.character 		= None
		self.item 				= None

	def set_description(self, room_description):
		self.description = room_description

	def set_name(self, room_name):
		self.name = room_name

	def set_character(self, character):
		self.character = character

	def get_description(self):
		"""Returns a string containing the description of the room"""
		return self.description

	def get_name(self):
		return self.name

	def get_character(self):
		return self.character

	def set_item(self, item):
		self.item = item

	def get_item(self):
		return self.item

	def describe(self):
		print(self.description)

	def link_room(self, room_to_link, direction):
		self.linked_rooms[direction] = room_to_link

	def get_details(self):
		print(self.name)
		print('-----------------')
		self.describe()
		#Print linked rooms
		for direction in self.linked_rooms:
			room = self.linked_rooms[direction]
			print('The ' + room.get_name() + ' is ' + direction)
		print('\n')
		#Print items
		item = self.item
		if item is not None:
			print('There is ' + item.get_name() + ' in here')
		else:
			print('There are no items in this room')
		#Print characters
		character = self.character
		if character is not None:
			character.describe()
		else:
			print('There is no one in this room')

	def move(self, direction):
		if direction in self.linked_rooms:
			return self.linked_rooms[direction]
		else:
			print('You cant go that way')
			return self
	