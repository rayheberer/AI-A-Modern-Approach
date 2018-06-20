class SimpleReflexAgent(object):
    def decide(self, location, dirt):
        if dirt:
            return 'Clean'
        if location.name == 'A':
            return 'Right'
        if location.name == 'B':
            return 'Left'

class StatefulReflexAgent(object):
    def __init__(self):
        self.moved = 0

    def decide(self, location, dirt):
        if dirt:
            return 'Clean'
        if self.moved == 1:
            return None
        if location.name == 'A':
            self.moved = 1
            return 'Right'
        if location.name == 'B':
            self.moved = 1
            return 'Left'