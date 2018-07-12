import random

class Square(object):
    def __init__(self, name):
        self.name = name
        
        # until put with a neighboring square, any movement goes nowhere
        self.left = self
        self.right = self
        self.up = self
        self.down = self

class SimpleVacuumWorld(object):
    def __init__(self, dirt_init='random', move_penalty=False, init_loc=None, perfect_information=False):
        # simple 2 square environment geography
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
        self.perfect_information = perfect_information
        
    def initialize_dirt(self):
        if self.dirt_init=='random':
            for square in self.squares:
                if random.random() > 0.5:
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
            i = random.randint(0, len(self.squares)-1)
            agent.location = self.squares[i]

    def performance(self, action):
        move = 0
        if self.move_penalty:
            if action is not None and action != 'Clean':
                move += 1

        dirt = sum([square.dirt for square in self.squares])
        return len(self.squares) - dirt - move
            
    def simulate(self, AgentObject):
        # initialize agent, time, performance measure
        agent = AgentObject()
        time = 0
        score = 0
        
        # initialize dirt and location
        self.initialize_dirt()
        self.initialize_agent_location(agent)
        
            
        # 1000 timestep lifetime
        while time < 1000:
            if self.perfect_information:
                percepts = [agent.location, self.A.dirt, self.B.dirt]
            else:
                percepts = [agent.location, agent.location.dirt]


            action = agent.decide(*percepts)
            
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

class UnknownVacuumWorld(SimpleVacuumWorld):
    def __init__(self, move_penalty=False, dirt_init='random', geography=None, bump_sensor=False):
        self.move_penalty = move_penalty

        self.dirt_init = dirt_init
        self.init_loc = None

        self.geography = geography
        if geography:
            self.construct_geography()

        self.bump_sensor = bump_sensor

    def construct_geography(self):
        """
        Example Geography (4x4 Grid, obstacle in center and corner):
                [['AA', 'AB', 'AC', None],
                 ['BA', 'BB', 'BC', 'BD'],
                 ['CA', None, 'CC', 'CD'],
                 ['DA', 'DB', 'DC', 'DD']]
        """
        if self.geography:
            self.squares = [Square(name) for row in self.geography for name in row if name is not None]
            self.x_coords = [row.index(name) for row in self.geography for name in row if name is not None]
            self.y_coords = [self.geography.index(row) for row in self.geography for name in row if name is not None]
            
            i = 0
            while i < len(self.squares)-1:
                j = i + 1
                x, y = self.x_coords[i], self.y_coords[i]

                while j < len(self.squares):
                    if self.x_coords[j] == x and self.y_coords[j] == y + 1:
                        self.squares[i].up = self.squares[j]
                        self.squares[j].down = self.squares[i]

                    if self.x_coords[j] == x + 1 and self.y_coords[j] == y :
                        self.squares[i].right = self.squares[j]
                        self.squares[j].left = self.squares[i]
                    j += 1

                i += 1

        else:
            self.squares = []
            A = Square('A')
            B = Square('B')
            self.squares.append(A)
            self.squares.append(B)

            A.right = B
            B.left = A

    def display_geography(self):
        rows = []
        for row in self.geography:
            row_list = []
            for square in row:
                if square:
                    row_list.append('|=|')
                else:
                    row_list.append('   ')
            rows.append(''.join(row_list))
            
        geo = '\n'.join(rows)
        print(geo)

    def simulate(self, AgentObject, **agent_kwargs):
        # initialize agent, time, performance measure
        agent = AgentObject(**agent_kwargs)
        time = 0
        cumulative_score = 0
        
        # default to simple geography
        if len(self.squares) == 0:
            self.construct_geography()
        # initialize dirt and location
        self.initialize_dirt()
        self.initialize_agent_location(agent)
        
        last_action = None
        last_location = None
        # 1000 timestep lifetime
        while time < 1000:
            score, last_action, last_location = self.step(agent, last_action, last_location)
            cumulative_score += score
            time += 1
            
        return cumulative_score

    def step(self, agent, last_action, last_location):
        if not self.bump_sensor:
            percepts = [agent.location, agent.location.dirt]
        else:
            if last_action in ['Left', 'Right', 'Up', 'Down'] and agent.location == last_location:
                bump = True
            else:
                bump = False
            percepts = [bump, agent.location.dirt]

        action = agent.decide(*percepts)
        last_action = action
        last_location = agent.location

        if action == 'Clean':
            agent.location.dirt = 0
        elif action == 'Left':
            agent.location = agent.location.left
        elif action == 'Right':
            agent.location = agent.location.right
        elif action == 'Up':
            agent.location = agent.location.up
        elif action == 'Down':
            agent.location = agent.location.down

        # performance measure: 1 point per clean square
        score = self.performance(action)

        return score, last_action, last_location