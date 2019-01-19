import pickle
import matplotlib.pyplot as plt
import numpy as np


a = pickle.load(open('results_housingprice.pkl', 'rb'))
wijken, steps, a = a[-1], a[-2], np.array(a[:-2])
density = np.array([np.round(x[1], 2) for x in a])
ratio = np.array([x[0] for x in a])
for i in range(len(density[0])):
    plt.figure(1)
    plt.plot(steps, list(density[:, i]), label=wijken[i])
    plt.figure(2)
    plt.plot(steps, list(ratio[:, i, 0]), label=wijken[i])
    plt.figure(3)
    plt.plot(steps, list(ratio[:, i, 1]), label=wijken[i])



plt.figure(1)
plt.title('Populatiedichtheid tegenover de weging van huizenprijs.')
plt.xlabel('Weging van huizenprijzen bij nut.')
plt.ylabel('Populatiedichtheid')
plt.ylim(0, 1.01)
plt.legend(fancybox=True, framealpha=0.5)
plt.savefig('density.png')
plt.figure(2)
plt.title('Percentage niet-Westerse agents per wijk.')
plt.xlabel('Weging van huizenprijzen bij nut.')
plt.ylabel('Percentage niet-Westerse agents.')
plt.ylim(0, 1.01)
plt.legend(fancybox=True, framealpha=0.5)
plt.savefig('niet_Westers.png')
plt.figure(3)
plt.title('Percentage Westerse agents per wijk.')
plt.xlabel('Weging van huizenprijzen bij nut.')
plt.ylabel('Percentage Westerse agents.')
plt.ylim(0, 1.01)
plt.legend(fancybox=True, framealpha=0.5)
plt.savefig('Westers.png')
plt.show(2)
