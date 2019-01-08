'''Class that will be used to house the model'''
import numpy as np
from Code import agent


class Model():
    def __init__(self, sizes, ratio):
        '''Initialize model with given specifications.'''
        self.neighborhoods = [[] for i in range(len(sizes))]
        self.ratio = ratio
        self.max = sizes
        self.zeros = []
        self.ones = []
        self.fill_neighborhoods(ratio, sizes)
        self.density = [r[0] + r[1] for r in ratio]

    def fill_neighborhoods(self, ratio, sizes):
        '''Fill the neighborhoods according to specified agent ratio.'''
        for i in range(len(self.ratio)):
            numberTypeZero = int(ratio[i][0] * self.max[i])
            numberTypeOne = int(ratio[i][1] * self.max[i])
            self.zeros.append(numberTypeZero)
            self.ones.append(numberTypeOne)
            self.fill_neighborhood(numberTypeZero, numberTypeOne, i)

    def fill_neighborhood(self, zeros, ones, neighborhoodID):
        '''Fills a single neighborhood with zeros and ones according to
        specified amount of zeros and ones.'''
        for i in range(zeros):
            self.neighborhoods[neighborhoodID].append(agent.Agent(0))
        for i in range(ones):
            self.neighborhoods[neighborhoodID].append(agent.Agent(1, 0.5))

    def update(self, n_IDs):
        '''updates ratios and density specs of model after switch'''
        for n_ID in n_IDs:
            self.ratio[n_ID][0] = self.zeros[n_ID] / self.max[n_ID]
            self.ratio[n_ID][1] = self.ones[n_ID] / self.max[n_ID]
            self.density[n_ID] = self.ratio[n_ID][0] + self.ratio[n_ID][1]
