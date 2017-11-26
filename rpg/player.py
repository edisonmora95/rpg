class Player():
	def __init__(self, name):
		self.name 		= name
		self.backpack = []
		self.life 		= 100

	def set_name(self, name):
		self.name = name

	def set_backpack(self, backpack):
		self.backpack = backpack

	def set_life(self, life):
		self.life = life

	def get_name(self):
		return self.name

	def get_backpack(self):
		return self.backpack

	def get_life(self):
		return self.life

	'''
		METHODS
	'''

	def collect_item(self, item):
		if len(self.backpack) < 3:
			self.backpack.append(item)
			return True
		else:
			print('Your backpack is full')
			return False

	def show_backpack(self):
		if len(self.backpack) == 0:
			print('Your backpack is empty')
		else:
			for item in self.backpack:
				print('	* ' + item.get_name())

	def drop_item_by_name(self, item_name):
		for item in self.backpack:
			if item.get_name() == item_name:
				self.backpack.remove(item)
				print(item.get_name() + ' was dropped from your backpack')
				return True
		return False

	def has_item(self, item_name):
		for item in self.backpack:
			if item.get_name() == item_name:
				return True
		return False