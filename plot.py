import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def cal_entropy(ratio):
    p = ratio[0]
    if p == 1 or p == 0:
        return 0
    return (-p * (np.log(p) / np.log(2))) - ((1 - p) * (np.log(1 - p) / np.log(2)))

a = pickle.load(open('results_housingprice.pkl', 'rb'))
wijken, steps, a = a[-1], a[-2], np.array(a[:-2])
S = pd.DataFrame({'Houseprice_Weight': steps})
density = np.array([np.round(x[1], 2) for x in a])
ratio = np.array([x[0] for x in a])
entropy = np.array([[cal_entropy(w) for w in r] for r in ratio])

# FOR TABLES
# entropy = pd.DataFrame(entropy)
# entropy.columns = [w + '_entropy'for w in wijken]
# entropy = S.join(entropy)
# ratioNW = pd.DataFrame(ratio[:,:,0])
# ratioNW.columns = [w + '_ratio_NW'for w in wijken]
# ratioNW = S.join(ratioNW)
# ratioW = pd.DataFrame(ratio[:,:,1])
# ratioW.columns = [w + '_ratio_W'for w in wijken]
# ratioW = S.join(ratioW)
# density = pd.DataFrame(density)
# density.columns = [w + '_density'for w in wijken]
# density = S.join(density)
#
# df_list = [entropy, ratioNW, ratioW, density]
# writer = pd.ExcelWriter('tabellen.xlsx')
# for i, df in enumerate(df_list):
#     df.to_excel(writer,'sheet{}'.format(i))
# writer.save()


for i in range(len(density[0])):
    plt.figure(1)
    plt.plot(steps, list(density[:, i]), label=wijken[i])
    plt.figure(2)
    plt.plot(steps, list(ratio[:, i, 0]), label=wijken[i])
    plt.figure(3)
    plt.plot(steps, list(ratio[:, i, 1]), label=wijken[i])
    plt.figure(4)
    plt.plot(steps, entropy[:, i], label=wijken[i])




plt.figure(1)
plt.title('Populatiedichtheid tegenover de weging van huizenprijs.')
plt.xlabel('Weging van huizenprijzen bij nutsberekening')
plt.ylabel('Populatiedichtheid')
plt.ylim(0, 1.01)
plt.legend(fancybox=True, framealpha=0.5)
plt.savefig('density.png')
plt.figure(2)
plt.title('Percentage niet-Westerse agents per wijk.')
plt.xlabel('Weging van huizenprijzen bij nutsberekening')
plt.ylabel('Percentage niet-Westerse agents.')
plt.ylim(0, 1.01)
plt.legend(fancybox=True, framealpha=0.5)
plt.savefig('niet_Westers.png')
plt.figure(3)
plt.title('Percentage Westerse agents per wijk.')
plt.xlabel('Weging van huizenprijzen bij nutsberekening')
plt.ylabel('Percentage Westerse agents.')
plt.ylim(0, 1.01)
plt.legend(fancybox=True, framealpha=0.5)
plt.savefig('Westers.png')
plt.figure(4)
plt.title('Entropie van de agents.')
plt.xlabel('Weging van huizenprijzen bij nutsberekening')
plt.ylabel('Entropie')
plt.ylim(0, 1.01)
plt.legend(fancybox=True, framealpha=0.5)
plt.savefig('Entropy_perwijk.png')
plt.show()
