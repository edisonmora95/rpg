import rpg
#Set up rooms
kitchen = rpg.Room('Kitchen')
kitchen.set_description('A dank and dirty room buzzing with flies.')

dining_hall = rpg.Room('Dining hall')
dining_hall.set_description('The hall for dining')

ballroom = rpg.Room('Ballroom')
ballroom.set_description('A room for balls')


#Link rooms
ballroom.link_room(dining_hall, 'east')
dining_hall.link_room(ballroom, 'west')
dining_hall.link_room(kitchen, 'north')
kitchen.link_room(dining_hall, 'south')


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
kitchen.set_item(cheese)
sword  = rpg.Item('sword')
dining_hall.set_item(sword)


backpack 		 				= []	#Backpack of the player
current_room 				= kitchen
characters_defeated = 0


dead = False

#Game loop
while dead == False or characters_defeated < 3:
	print('\n')
	current_room.get_details()
	#Get character in room
	character = current_room.get_character()
	item 			= current_room.get_item()

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
			fight_with = input()
			#Check if player has item
			if fight_with in backpack:
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
	elif command == 'pick up':
		if item is not None:
			backpack.append(item)
			current_room.set_item(None)
		else:
			print('There are no items in this room')

