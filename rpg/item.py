class Item():
	def __init__(self):
		self.name = None
		self.description = None

	def __init__(self, item_name):
		self.name = item_name
		self.description = None

	def set_name(self, item_name):
		self.name = item_name

	def set_description(self, item_description):
		self.description = item_description

	def get_name(self):
		return self.name

	def get_description(self):
		return self.description

	