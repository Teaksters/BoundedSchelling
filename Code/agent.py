'''The class that will be used for every agent in the model.'''


class Agent():
    def __init__(self, type=0, tolerance=0, empty=True):
        self.type = type
        self.tolerance = tolerance
        self.empty = empty
