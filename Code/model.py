'''Class that will be used to house the model'''
import numpy as np
from Code import agent


class Model():
    def __init__(self, sizes, ratio):
        '''Initialize model with given specifications.'''
        self.neighborhoods = np.array([self.create_neighborhood(size)
                                      for size in sizes])
        self.ratio = ratio
        self.fill_neighborhoods(ratio)
        self.density = [r[0] + r[1] for r in ratio]

    def create_neighborhood(self, size):
        '''Create an empty neighborhood of specified sizes.'''
        return np.array([agent.Agent() for i in range(size)])

    def fill_neighborhoods(self, ratio):
        '''Fill the neighborhoods according to specified agent ratio.'''
        for i in range(len(self.ratio)):
            numberTypeZero = int(ratio[i][0] * len(self.neighborhoods[i]))
            numberTypeOne = int(ratio[i][1] * len(self.neighborhoods[i]))
            self.fill_neighborhood(numberTypeZero, numberTypeOne, i)

    def fill_neighborhood(self, zeros, ones, neighborhoodID):
        '''Fills a single neighborhood with zeros and ones according to
        specified amount of zeros and ones.'''
        for n in self.neighborhoods[neighborhoodID][:zeros]:
            n.empty = False
            n.type = 0
            n.tolerance = 0
        for n in self.neighborhoods[neighborhoodID][zeros:zeros + ones]:
            n.empty = False
            n.type = 1
            n.tolerance = 0
