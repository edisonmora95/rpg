from character import Enemy

dave = Enemy('Dave', 'A smelly zombie')
dave.set_conversation('Aaahh')
dave.set_weakness('cheese')
dave.talk()

print('What will you fight with?')
fight_with = input()
dave.fight(fight_with)


