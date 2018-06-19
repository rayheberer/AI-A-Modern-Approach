class SimpleReflexAgent(object):
    def decide(self, location, dirt):
        if dirt:
            return 'Clean'
        if location.name == 'A':
            return 'Right'
        if location.name == 'B':
            return 'Left'