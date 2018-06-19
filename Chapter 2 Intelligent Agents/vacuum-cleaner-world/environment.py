import numpy as np

class Square(object):
    def __init__(self, name):
        self.name = name
        
        # until put with a neighboring square, any movement goes nowhere
        self.left = self
        self.right = self
        self.up = self
        self.down = self

class SimpleVacuumWorld(object):
    def __init__(self):
        self.squares = []
        self.A = Square('A')
        self.B = Square('B')
        self.squares.append(self.A)
        self.squares.append(self.B)

        self.A.right = self.B
        self.B.left = self.A
        
    def initialize_dirt(self, method='random', p=0.5):
        if method=='random':
            for square in self.squares:
                if np.random.random() > 0.5:
                    square.dirt = 1
                else:
                    square.dirt = 0
                    
    def initialize_agent_location(self, agent):
        i = np.random.randint(len(self.squares))
        
        agent.location = self.squares[i]
            
    def simulate(self, agent, **dirt_init):
        time = 0
        score = 0
        
        # initialize dirt and location randomly
        self.initialize_dirt(**dirt_init)
        self.initialize_agent_location(agent)
        
            
        # 1000 timestep lifetime
        while time < 1000:
            action = agent.decide(agent.location, agent.location.dirt)
            
            if action == 'Clean':
                agent.location.dirt = 0
            elif action == 'Left':
                agent.location = agent.location.left
            elif action == 'Right':
                agent.location = agent.location.right
            
            # performance measure: 1 point per clean square, per timestep
            score += (2 - self.A.dirt - self.B.dirt)
            time += 1
            
        return score