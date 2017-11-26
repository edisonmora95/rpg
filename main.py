import rpg

def pick_up_item(item_selected, player, current_room):
	'''Picks up an item from the room and adds it to the player's backpack'''
	item = current_room.get_item_by_name(item_selected)
	if item is not None:
		if player.collect_item(item):
			current_room.remove_item(item)
	else:
		print('There no such item in this room')

#Set up rooms
entrance = rpg.Room('Entrance')
entrance.set_description('The entrance of the mansion')

corridor = rpg.Room('Corridor')
corridor.set_description('A long corridor')

lounge = rpg.Room('Lounge')
lounge.set_description('A room full of furniture')

kitchen = rpg.Room('Kitchen')
kitchen.set_description('A dank and dirty room buzzing with flies.')
kitchen.set_state('locked')

dining_hall = rpg.Room('Dining hall')
dining_hall.set_description('The hall for dining')

ballroom = rpg.Room('Ballroom')
ballroom.set_description('A room for balls')


#Link rooms
entrance.link_room(corridor, 'north')
corridor.link_room(dining_hall, 'west')
corridor.link_room(lounge, 'east')
dining_hall.link_room(corridor, 'east')
dining_hall.link_room(kitchen, 'north')
kitchen.link_room(dining_hall, 'south')
lounge.link_room(corridor, 'west')


#Set up enemies
dave = rpg.Enemy('Dave', 'A smelly zombie')
dave.set_conversation('Brrlgrh... rgrhl... brains...')
dave.set_weakness('cheese')
dining_hall.set_character(dave)

mike = rpg.Enemy('Mike', 'Another zombie')
mike.set_conversation('Brrlgrh... rgrhl... brains...')
mike.set_weakness('cheese')
kitchen.set_character(mike)


#Set up items
cheese = rpg.Item('cheese')
knife	 = rpg.Item('knife')
sword	 = rpg.Item('sword')
shield = rpg.Item('shield')
wand	 = rpg.Item('wand')
key		 = rpg.Item('key')
note	 = rpg.Item('note')
dining_hall.add_item(sword)
dining_hall.add_item(key)
lounge.add_item(note)
lounge.add_item(shield)
kitchen.add_item(cheese)
kitchen.add_item(knife)


#Main
print('********************************************************')
name 	 = input('Enter your name: ')
player = rpg.Player(name)
print('Welcome ' + player.get_name())

backpack 		 				= []	#Backpack of the player
current_room 				= entrance
characters_defeated = 0


dead = False

#Game loop
while dead == False or characters_defeated < 3:
	print('\n')
	print('----------------------')
	current_room.get_details()
	#Get character in room
	character = current_room.get_character()

	#Get command
	command = input('>')
	#Move
	if command in ['north', 'south', 'east', 'west']:
		current_room = current_room.move(command)
	#Talk
	elif command == 'talk':
		if character is not None:
			character.talk()
		else:
			print('There is no one in this room to ' + command)
	#Fight
	elif command == 'fight':
		if character is not None:
			print('What will you fight with?')
			player.show_backpack()
			fight_with = input('>')
			#Check if player has item
			if player.has_item(fight_with):
				result = character.fight(fight_with)
				#Check result
				if result is False:
					print('You lost')
					dead = True
				else:
					print('You won the fight!')
					current_room.set_character(None)
					characters_defeated = characters_defeated + 1
			else:
				print('You dont have that item in your backpack')
		else:
			print('There is no one in this room to ' + command)
	#Pick up item
	elif command.startswith('pick up'):
		if not current_room.has_items():
			print('There are no items in this room')
		else:			
			words = command.split(' ')	#Array of words from the command
			#If the player didn't enter the item to pickup
			if len(words) == 2:
				print('What do you want to pick up?')
				current_room.show_items()
				item_selected = input('>')
				pick_up_item(item_selected, player, current_room)
			else:	
				item_selected = words[2]
				pick_up_item(item_selected, player, current_room)
	#Check
	elif command.startswith('check backpack'):
		player.show_backpack()
