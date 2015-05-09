__author__ = 'Liam'
from random import randrange

from room import *


class Player:
    """The Player object, with associated variables and methods. This is you!
    """

    def __init__(self, location):
        """When initialising the character, we'll later give the player the
        choice of a name and spirit animal type, which will affect the chance
        of certain events/room types/items. For now, the inventory and location
        are all that actually matter.

        self.name = input('Hey kid, it\'s your Spirit Animal. What\'s your '
                          'name?\n>')
        self.spirit = input('{} eh? Cool, I guess. So, currently I don\'t have'
                            ' any shape or form. What should I be?\n>'
                            .format(self.name))"""
        self.name = 'Billy Boy'
        self.spirit = 'Boar'
        self.inventory = []
        self.location = location
        self.actions = {'1': self.search, '2': self.grab, '3': self.gurgle}

    def forward(self):
        pass

    def backward(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def grab(self):
        """Grabs a random item from the room, if any exist. Hey, you're a baby,
        you're lucky to be able to grab anything.
        """
        if len(self.location.contents) == 0:
            print('Hate to break it to you, but there\'s nothing to grab.')
        elif random() >= .75:
            item = self.location.contents[
                randrange(len(self.location.contents))]
            self.inventory.append(item)
            self.location.remove(item)
            print('Nice one, you actually managed to grab the {}! '
                  'I\'m not even angry, I\'m impressed.'.format(item))
        else:
            print('Well, at least you flailed in an impressive fashion.')

    def gurgle(self, enemy):
        print('Look at that, you can laugh. The {} noticed, too.'
              .format(self.name, enemy.species))

    def search(self):
        print('\nYou found the following items. Neat.\n{}'
              .format(', '.join(self.location.contents)))


def main():
    """The main logic loop for the game, and it's pretty simple. Loop and a
    half for the win. Initiates the player in a Living Room. Needs tidying.
    """
    player = Player(LivingRoom())
    escaping = True

    print('Alright kid, it\'s you and me on a grand adventure. We\'re '
          'currently in the {}, and I can see {} possible exits. You can '
          'search the room or try exploring, if you like.'
          .format(player.location.name, player.location.exits))

    while escaping:
        # need to replace hard list with extract from player.actions
        action = input('\nWhat now?\n\n1. Search\t2. Grab\t3. Gurgle\n>')

        if action in player.actions.keys():
            player.actions[action]()


main()


# print(c.contents)
#  a.gurgle(b)