'''The class that will be used for every agent in the model.'''


class Agent():
    def __init__(self, type, tolerance=1):
        self.type = type
        self.tolerance = tolerance
