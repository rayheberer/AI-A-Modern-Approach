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
    def __init__(self, sensor='location'):
        self.movements = []
        self.directions_explored = {}
        self.last_location = None
        self.last_action = None
        self.backtracking = {'Up': 'Down', 
                             'Down': 'Up', 
                             'Left': 'Right', 
                             'Right': 'Left'}

        if sensor == 'location':
            self.decide = self.decide_location
        else:
            self.x = 0
            self.y = 0
            self.decide = self.decide_bump

    def decide_location(self, location, dirt):
        if dirt:
            return 'Clean'
        
        new_loc = False
        if location.name != self.last_location and self.last_location is not None:
            self.movements.append(self.last_action)
            new_loc = True

        if location.name in self.directions_explored.keys():
            if new_loc and self.backtracking[self.last_action] in self.directions_explored[location.name]:
                self.directions_explored[location.name].remove(self.backtracking[self.last_action])

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

    def decide_bump(self, bump, dirt):
        if dirt:
            return 'Clean'

        new_loc = False
        if not bump:
            self.update_coords(self.last_action)
            if self.last_location:
                self.movements.append(self.last_action)
                new_loc = True

        if (self.x, self.y) in self.directions_explored.keys():
            if new_loc and self.backtracking[self.last_action] in self.directions_explored[(self.x, self.y)]:
                self.directions_explored[(self.x,  self.y)].remove(self.backtracking[self.last_action])

            if len(self.directions_explored[(self.x, self.y)]) > 0:
                action = self.directions_explored[(self.x, self.y)][0]
            elif len(self.movements) > 0:
                self.last_location = None
                last_move = self.movements.pop()
                action = self.backtracking[last_move]
                self.last_action = action
                return action
            else:
                return None
        else:
            directions = ['Up', 'Left', 'Down', 'Right']
            if self.last_action:
                directions.remove(self.backtracking[self.last_action])

            self.directions_explored[(self.x, self.y)] = directions
            action = self.directions_explored[(self.x, self.y)][0]

        self.directions_explored[(self.x, self.y)].remove(action)
        self.last_location = (self.x, self.y)
        self.last_action = action

        return action

    def update_coords(self, action):
        if action == 'Up':
            self.y += 1
        elif action == 'Down':
            self.y -= 1
        elif action == 'Right':
            self.x += 1
        elif action == 'Left':
            self.x -= 1