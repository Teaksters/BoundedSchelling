from Code import schelling
import numpy as np
import pickle


def main():
    data = np.loadtxt('AMS_Bevolking_data_2014.csv',
                      dtype=str,
                      delimiter=',',
                      skiprows=2)
    cap, r, wijken = prep(data)
    cap /= 100
    housingp = np.linspace(0, 1, num=11, endpoint=True)
    res = []
    for price in housingp:
        print(price)
        temp_dens = []
        temp_ratio = []
        for i in range(10):
            a = schelling.Schelling(cap, r)
            a.p_const = price
            a.run(10000)
            temp_dens.append(a.model.density)
            temp_ratio.append(a.model.ratio)
        res.append([np.mean(temp_ratio, axis=0), np.mean(temp_dens, axis=0)])
    res.append(housingp)
    res.append(wijken)
    pickle.dump(np.array(res), open('results_housingprice.pkl', 'wb'))


def prep(data):
    wijken = data[:, 0]
    cap = np.array([int(((int(d[1]) + int(d[2])) * 1.2)) for d in data])
    r = np.array([[d[1], d[2]] for d in data], dtype=int)
    r = np.array([r[i] / cap[i] for i in range(len(cap))])
    cap = cap / 2.25
    return cap, r, wijken


if __name__ == '__main__':
    main()
