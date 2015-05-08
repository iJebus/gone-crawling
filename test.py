__author__ = 'Liam'

from application import Player, LivingRoom

player = Player(LivingRoom())

print('Location: ' + player.location.name)
print(player.location.exits)
player.search()
player.grab()
print(player.location.contents)
print(player.inventory)