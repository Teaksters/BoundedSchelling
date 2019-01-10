from Code import schelling
import numpy as np


def main():
    a = schelling.Schelling([50, 100, 80, 305], [[0.5, 0.2], [0.1, 0.2], [0.5, 0.3], [0.5, 0.3]])
    a.run(10000)
    print(np.array([[agent.type for agent in n] for n in a.model.neighborhoods]))
    print(a.model.density)

if __name__ == '__main__':
    main()
