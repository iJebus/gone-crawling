__author__ = 'Liam'

from random import random

from enemy import Dog


class Room:
    def __init__(self, name, interior, contents):
        self.name = name
        self.interior = interior
        self.contents = contents
        # self.exits = randrange(1, 5)

    def add(self, item):
        self.contents.append(item)

    def remove(self, item):
        self.contents.remove(item)


class LivingRoom(Room):
    def __init__(self):
        super().__init__('Living Room', True, ['Arm-chair', 'dog biscuit'])
        self.exits = [Kitchen, Backyard]


class Kitchen(Room):
    def __init__(self):
        super().__init__('Kitchen', True, ['crumbs', 'water bowl'])
        if random() <= .5:
            self.contents.append(Dog)


class Backyard(Room):
    def __init__(self):
        super().__init__('Backyard', False, ['dirt', 'flowers'])