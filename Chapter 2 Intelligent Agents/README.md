# Chapter 2 Implementation Exercises

## Vacuum-Cleaner World

__2.9__ Implement a performance-measuring environment simulator for the vacuum-cleaner world depicted in Figure 2.2 and specified on page 38. Your implementation should be modular so that the sensors, actuators, and environment characteristics (size, shape, dirt placement, etc.) can be changed easily. (_Note:_ for some choices of programming language and operating system there are already implementations in the [online code repository](http://aima.cs.berkeley.edu/code.html).)

__2.10__ Consider a modified version of the vacuum environment in Exercise 2.9, in which the agent is penalized one point for each movement.
__a.__ Can a simple reflex agent be perfectly rational for this environment? Explain.
__b.__ What about a reflex agent with state? Design such an agent.
__c.__ How do your answers to __a__ and __b__ change if the agent's percepts give it the clean/dirty status of every square in the environment?

__2.11__ Consider a modified version of the vacuum environment in Exercise 2.9, in which the geography of the environment - its extent, boundaries, and obstacles - is unknown, as is the initial dirt configuration. (The agent can go _Up_ and _Down_ as well as _Left_ and _Right_.)
__a.__ Can a simple reflex agent be perfectly rational for this environment? Explain.
__b.__ Can a simple reflex agent with a _randomized_ agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.
__c.__ Can you design an environment in which your randomized agent will perform poorly? Show your results.
__d.__ Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?

__2.12__ Repeat Exercise 2.11 for the case in which the location sensor is replaced with a "bump" sensor that detects the agent's attempts to move into an obstacle or to cross the boundaries of the environment. Suppose the bump sensor stops working; how should the agent behave?

__2.13__ The vacuum environments in the preceding exercises have all been deterministic. Discuss possible agent programs for each of the following stochastic versions:
__a.__ Murphy's law: twenty-five percent of the time, the _Suck_ action fails to clean the flow if it is dirty and deposits dirt onto the floor if the floor is clean. How is your agent program affected if the dirt sensor gives the wrong answer 10% of the time?
__b.__ Small children: At each time step, each clean square has a 10% chance of becoming dirty. Can you come up with a rational agent design for this case?