class Room():

	'''
		CONSTRUCTORS
	'''
	def __init__(self):
		self.name 			  = None
		self.description  = None
		self.state 				= 'unlocked'
		self.linked_rooms = {}
		self.character 	  = None
		self.items 				= []

	def __init__(self, room_name):
		self.name 			  = room_name
		self.description  = None
		self.state 				= 'unlocked'
		self.linked_rooms = {}
		self.character 		= None
		self.items 				= []

	'''
		GETTERS & SETTERS
	'''
	def set_name(self, room_name):
		self.name = room_name

	def set_description(self, room_description):
		self.description = room_description

	def set_state(self, state):
		self.state = state

	def set_character(self, character):
		self.character = character

	def get_name(self):
		return self.name
	
	def get_description(self):
		"""Returns a string containing the description of the room"""
		return self.description

	def get_state(self):
		return self.state

	def get_character(self):
		return self.character

	def get_items(self):
		return self.items

	def get_item_by_name(self, item_name):
		for item in self.items:
			if item.get_name() == item_name:
				return item
		return None

	def remove_item(self, item):
		self.items.remove(item)

	'''	
		METHODS
	'''

	def describe(self):
		print(self.description)

	def link_room(self, room_to_link, direction):
		self.linked_rooms[direction] = room_to_link

	def get_details(self):
		"""Prints the room's name, description, linked rooms, items and characters"""
		print(self.name)
		print('----------------------')
		self.describe()
		#Print linked rooms
		self.show_rooms()
		#Print items
		self.show_items()
		#Print characters
		character = self.character
		if character is not None:
			character.describe()
		else:
			print('There is no one in this room')

	def move(self, direction):
		if direction in self.linked_rooms:
			room = self.linked_rooms[direction]
			if room.get_state() == 'unlocked':
				return room
			elif room.get_state() == 'locked':
				print('It\'s locked')
				return self
		else:
			print('You cant go that way')
			return self
	
	def add_item(self, item):
		"""Adds an item to the room if the room has less than 3 items"""
		if len(self.items) < 3 :
			self.items.append(item)
		else:
			print('You reached the limit of items of the room')

	def has_items(self):
		return len(self.items) > 0

	def show_items(self):
		if not self.items:
			print('There are no items in this room')
			return
		print('Items in this room:')
		for item in self.items:
			print('	* ' + item.get_name())

	def show_rooms(self):
		for direction in self.linked_rooms:
			room = self.linked_rooms[direction]
			print('The ' + room.get_name() + ' is ' + direction + ' (' + room.get_state() + ')')
		print('\n')