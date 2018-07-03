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

class DepthStatefulReflexAgent(object):
    def __init__(self):
        self.movements = []
        self.directions_explored = {}
        self.last_location = None
        self.last_action = None
        self.backtracking = {'Up': 'Down', 
                             'Down': 'Up', 
                             'Left': 'Right', 
                             'Right': 'Left'}

    def decide(self, location, dirt):
        if dirt:
            return 'Clean'

        if location.name != self.last_location and self.last_location is not None:
            self.movements.append(self.last_action)

        if location.name in self.directions_explored.keys():
            if len(self.directions_explored[location.name]) > 0:
                action = self.directions_explored[location.name][0]
            elif len(self.movements) > 0:
                self.last_location = None
                last_move = self.movements.pop()
                return self.backtracking[last_move]
            else:
                return None
        else:
            directions =  ['Up', 'Left', 'Down', 'Right']
            if self.last_action:
                directions.remove(self.backtracking[self.last_action])

            self.directions_explored[location.name] = directions
            action = self.directions_explored[location.name][0]

        self.directions_explored[location.name].remove(action)
        self.last_location = location.name
        self.last_action = action

        return action