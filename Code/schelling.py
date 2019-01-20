from Code import model
import random
import copy
import time
from progressbar import progressbar


class Schelling():
    '''Object that runs Schelling model.'''
    def __init__(self, sizes, ratios):
        self.model = model.Model(sizes, ratios)
        self.ideal = 0.5
        self.all_same = 0.8
        self.p_const = 0

    def run(self, iterations):
        '''Run the Schelling model for specified iterations'''
        for i in progressbar(range(iterations)):
            a_ID, n_ID = self.pick_random_agent()
            if not self.toleranceCheck(a_ID, n_ID):
                self.move_agent(a_ID, n_ID)

    def pick_random_agent(self):
        '''Pick a random non-empty agent and return it and its location.'''
        n_ID = random.randint(0, len(self.model.neighborhoods) - 1)
        if len(self.model.neighborhoods[n_ID]) == 0:
            _, n_ID = self.pick_random_agent()
        a_ID = random.randint(0, len(self.model.neighborhoods[n_ID]) - 1)
        return a_ID, n_ID

    def toleranceCheck(self, a_ID, n_ID, ID=True):
        '''Returns True if agent is happy at current location,
        else returns False. Needs more precise utility function.'''
        if ID:
            agent = self.model.neighborhoods[n_ID][a_ID]
        else:
            agent = a_ID
        utility = self.utility(n_ID, agent)
        return agent.tolerance >= utility

    def move_agent(self, a_ID, n_ID):
        '''Move agent to new suitable location if possible.'''
        agent = self.model.neighborhoods[n_ID].pop(a_ID)
        newN_ID = self.find_new_location(agent, n_ID)
        self.model.neighborhoods[newN_ID].append(agent)
        if agent.type is 0:
            self.model.zeros[n_ID] -= 1
            self.model.zeros[newN_ID] += 1
        else:
            self.model.ones[n_ID] -= 1
            self.model.ones[newN_ID] += 1
        self.model.update([n_ID, newN_ID])

    def find_new_location(self, agent, n_ID, full=set()):
        '''Find a new suitable place if agent is unhappy.'''
        Choice = [i for i in range(len(self.model.ratio)) if i not in full]
        temp = copy.copy(agent.tolerance)
        options = copy.copy(Choice)
        random.shuffle(options)
        newN_ID = options.pop()
        while not self.toleranceCheck(agent, newN_ID, False):
            # If no place is found search for next best place.
            if len(options) == 0:
                options = copy.copy(Choice)
                agent.tolerance += 0.01
                # Don't move the agent if it does not improve his situation
                if agent.tolerance >= self.utility(n_ID, agent):
                    agent.tolerance = temp
                    return n_ID
            newN_ID = options.pop()
        if self.model.density[newN_ID] >= 1:
            full.add(newN_ID)
            newN_ID = self.find_new_location(agent, n_ID, full)
        # reset agents possibly altered tolerance
        agent.tolerance = temp
        return newN_ID

    def utility(self, n_ID, agent):
        '''Calculates utility for 2 types of agents, with one only looking at
        housing prices and the other also taking into account the neighborhood
        agent blend.'''
        if agent.type is 0:
            return self.willingness(n_ID, agent) - \
                   self.p_const * self.model.density[n_ID]
        else:
            return 1 - self.p_const * self.model.density[n_ID]

    def willingness(self, n_ID, agent):
        '''Calculate the agent type component of the utility.'''
        if self.model.density[n_ID] == 0:
            alike = 1
            alike *= self.model.max[n_ID]
        else:
            alike = self.model.ratio[n_ID][agent.type]
            alike *= self.model.max[n_ID]
        n = self.ideal * self.model.max[n_ID]
        # Calculate willingness to pay
        if n >= alike:
            n_pref = (alike / n)
        else:
            n_pref = (2 - self.all_same) + \
                   (((self.all_same - 1) * alike) / n)
        return n_pref
