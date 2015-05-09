__author__ = 'Liam'


class Enemy:
    def __init__(self, will, perception, intelligence):
        self.will = will
        self.perception = perception
        self.intelligence = intelligence
        self.disabled = False

    def alert(self):
        self.will += 10
        self.perception += 10


class Dog(Enemy):
    def __init__(self):
        super().__init__(75, 100, 50)
        self.species = 'dog'
        self.name = 'Fido'