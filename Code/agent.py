'''The class that will be used for every agent in the model.'''
import numpy as np


class Agent():
    def __init__(self, type, mu=0.5, sigma=0.5):
        self.type = type
        self.tolerance = abs(np.random.normal(mu, sigma))
        if self.tolerance > 1:
            self.tolerance = 1
