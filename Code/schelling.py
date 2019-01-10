from Code import model
import random
import copy


class Schelling():
    def __init__(self, sizes, ratios):
        self.model = model.Model(sizes, ratios)

    def run(self, iterations):
        '''Run the Schelling model for specified iterations'''
        for i in range(iterations):
            a_ID, n_ID = self.pick_random_agent()
            if not self.toleranceCheck(a_ID, n_ID):
                self.move_agent(a_ID, n_ID)

    def pick_random_agent(self):
        '''Pick a random non-empty agent and return it and its location.'''
        n_ID = random.randint(0, len(self.model.neighborhoods) - 1)
        a_ID = random.randint(0, len(self.model.neighborhoods[n_ID]) - 1)
        return a_ID, n_ID

    def toleranceCheck(self, a_ID, n_ID, ID=True):
        '''Returns True if agent is happy at current location,
        else returns False. Needs more precise utility function.'''
        if ID:
            agent = self.model.neighborhoods[n_ID][a_ID]
        else:
            agent = a_ID
        utility = self.model.ratio[n_ID][agent.type - 1]
        utility /= self.model.density[n_ID]
        return agent.tolerance >= utility

    def move_agent(self, a_ID, n_ID):
        '''Move agent to new suitable location if possible.'''
        agent = self.model.neighborhoods[n_ID].pop(a_ID)
        newN_ID = self.find_new_location(agent)
        self.model.neighborhoods[newN_ID].append(agent)
        if agent.type is 0:
            self.model.zeros[n_ID] -= 1
            self.model.zeros[newN_ID] += 1
        else:
            self.model.ones[n_ID] -= 1
            self.model.ones[newN_ID] += 1
        self.model.update([n_ID, newN_ID])

    def find_new_location(self, agent, full=set()):
        '''Find a new suitable place if agent is unhappy.'''
        Choice = [i for i in range(len(self.model.ratio)) if i not in full]
        temp = agent.tolerance
        options = copy.copy(Choice)
        random.shuffle(options)
        newN_ID = options.pop()
        while not self.toleranceCheck(agent, newN_ID, False):
            # If no place is found search for next best place.
            if len(options) == 0:
                options = copy.copy(Choice)
                agent.tolerance += 0.01
            newN_ID = options.pop()
        if self.model.density[newN_ID] == 1:
            full.add(newN_ID)
            newN_ID = self.find_new_location(agent, full)
        # reset agents possibly altered tolerance
        agent.tolerance = temp
        return newN_ID
