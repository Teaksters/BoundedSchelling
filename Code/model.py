'''Class that will be used to house the model'''
from Code import agent
import copy


class Model():
    def __init__(self, sizes, ratio):
        '''Initialize model with given specifications.'''
        self.neighborhoods = [[] for i in range(len(sizes))]
        self.ratio = copy.copy(ratio)
        self.max = copy.copy(sizes)
        self.zeros = []
        self.ones = []
        self.density = [r[0] + r[1] for r in ratio]
        self.fill_neighborhoods(ratio, sizes)

    def fill_neighborhoods(self, ratio, sizes):
        '''Fill the neighborhoods according to specified agent ratio.'''
        for i in range(len(self.ratio)):
            numberTypeZero = int(ratio[i][0] * self.max[i])
            numberTypeOne = int(ratio[i][1] * self.max[i])
            self.zeros.append(numberTypeZero)
            self.ones.append(numberTypeOne)
            self.fill_neighborhood(numberTypeZero, numberTypeOne, i)
        self.update(list(range(len(self.neighborhoods))))

    def fill_neighborhood(self, zeros, ones, neighborhoodID):
        '''Fills a single neighborhood with zeros and ones according to
        specified amount of zeros and ones.'''
        for i in range(zeros):
            self.neighborhoods[neighborhoodID].append(agent.Agent(0))
        for i in range(ones):
            self.neighborhoods[neighborhoodID].append(agent.Agent(1))

    def update(self, n_IDs):
        '''updates ratios and density specs of model after switch'''
        for n_ID in n_IDs:
            nr_agents = self.zeros[n_ID] + self.ones[n_ID]
            if nr_agents > 0:
                self.ratio[n_ID][0] = self.zeros[n_ID] / nr_agents
                self.ratio[n_ID][1] = self.ones[n_ID] / nr_agents
                self.density[n_ID] = nr_agents / self.max[n_ID]
            else:
                self.ratio[n_ID][0] = 0.5
                self.ratio[n_ID][1] = 0.5
                self.density[n_ID] = 0
