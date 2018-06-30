import random

class SimpleReflexAgent(object):
    def decide(self, location, dirt):
        if dirt:
            return 'Clean'
        elif location.name == 'A':
            return 'Right'
        elif location.name == 'B':
            return 'Left'

class SimpleReflexAgentUnknown(object):
    def __init__(self, direction):
        """Will clean current square, or otherwise move in a specified direction"""
        self.direction = direction

    def decide(self, location, dirt):
        if dirt:
            return 'Clean'
        else:
            return self.direction

class FullInfoReflexAgent(object):
    def decide(self, location, dirtA, dirtB):
        if ((location.name == 'A' and dirtA)
            or (location.name == 'B' and dirtB)):
            return 'Clean'
        elif location.name == 'A' and dirtB:
            return 'Right'
        elif location.name == 'B' and dirtA:
            return 'Left'

class StatefulReflexAgent(object):
    def __init__(self):
        self.moved = 0

    def decide(self, location, dirt):
        if dirt:
            return 'Clean'

        elif self.moved == 0:
            if location.name == 'A':
                self.moved = 1
                return 'Right'
            elif location.name == 'B':
                self.moved = 1
                return 'Left'

class RandomizedReflexAgent(object):
    def decide(self, location, dirt):
        if dirt:
            return 'Clean'
        else:
            moves = ['Left', 'Right', 'Up', 'Down']
            return random.choice(moves)

class StatefulReflexAgentUnknown(object):
    def __init__(self):
        self.squares_visited = []
        self.directions_explored = {}

    def decide(self, location, dirt):
        pass