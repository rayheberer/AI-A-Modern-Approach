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
    def __init__(self, dirt_init='random', move_penalty=False, init_loc=None):
        self.squares = []
        self.A = Square('A')
        self.B = Square('B')
        self.squares.append(self.A)
        self.squares.append(self.B)

        self.A.right = self.B
        self.B.left = self.A

        # simulation params
        self.dirt_init = dirt_init
        self.move_penalty = move_penalty
        self.init_loc = init_loc
        
    def initialize_dirt(self):
        if self.dirt_init=='random':
            for square in self.squares:
                if np.random.random() > 0.5:
                    square.dirt = 1
                else:
                    square.dirt = 0

        elif self.dirt_init=='dirty':
            for square in self.squares:
                square.dirt = 1

        elif self.dirt_init=='clean':
            for square in self.squares:
                square.dirt = 0

        else:
            for square, value in zip(self.squares, self.dirt_init):
                square.dirt = value
                    
    def initialize_agent_location(self, agent):

        if self.init_loc=='A':
            agent.location = self.A
        elif self.init_loc=='B':
            agent.location = self.B
        else:
            i = np.random.randint(len(self.squares))
            agent.location = self.squares[i]

    def performance(self, action):
        move = 0
        if self.move_penalty:
            if action is not None and action != 'Clean':
                move += 1

        dirt = sum([square.dirt for square in self.squares])
        return len(self.squares) - dirt - move
            
    def simulate(self, AgentObject):
        agent = AgentObject()
        time = 0
        score = 0
        
        # initialize dirt and location
        self.initialize_dirt()
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
            score += self.performance(action)
            time += 1
            
        return score