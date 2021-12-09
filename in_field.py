import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import argrelmin

#from find_curves_data import light
from data_ii import light
from data_ii import sequence
from scipy.signal import argrelmin

if __name__ == "__main__":


    light_old = light

    light = []

    #for l in light[0:2:1]:
    for l in light_old:
        l = np.array(l)

        indice = np.where(l>90)[0][0]

        #plt.plot(l[indice:],'-')

        light.append(l[indice:indice+50])
        #

    light = np.array(light)
    l_median= np.median(light,axis=0)
    l_median=l_median/np.sum(l_median)
    print(np.mean(light,axis=0))
    plt.plot(light.T,'-.x',alpha=0.3)
    plt.plot(np.mean(light,axis=0),'-o')
    plt.plot(np.median(light,axis=0),'-v')
    plt.show()

    sequence = np.array(sequence)

    regular = np.convolve(sequence,l_median)

    plt.plot(sequence)
    plt.plot(regular)
    plt.show()




    """ids = np.where(light<=25)[0]

    print(ids)

    mask = np.array([25,25,99,99])
    mask = mask/np.sum(mask)

    regular = np.convolve(light,mask)

    plt.plot(range(light.shape[0]),light)
    plt.plot(ids,light[ids],'o')
    plt.plot(3+np.arange(regular.shape[0]),regular)
    plt.show()"""

    """curves = []

    curves.append(light[71-2:85+2])
    curves.append(light[130-2:144+2])
    curves.append(light[251-2:265+2])
    curves.append(light[418-2:432+2])
    curves.append(light[480-2:494+2])
    curves.append(light[594-2:608+2])
    curves.append(light[772-2:786+2])
    curves.append(light[823-2:837+2])
    curves.append(light[947-2:961+2])
    curves.append(light[1003-2:1017+2])
    curves.append(light[1303-2:1317+2])
    curves.append(light[1358-2:1372+2])
    curves.append(light[1448-2:1462+2])
    curves.append(light[1565-2:1579+2])
    curves.append(light[1658-2:1672+2])
    #curves.append(light[1719:1733])

    curves = np.array(curves).T

    print(curves.shape)

    median_curve = np.median(curves,axis=1)


    print(median_curve)

    plt.plot(curves,'--')
    plt.plot(median_curve,'-bo')
    plt.show()

    median_curve = median_curve/np.sum(median_curve)

    regular = np.convolve(light,median_curve)

    plt.plot(light,'-o')
    plt.plot(regular,'-o')
    plt.show()"""


    """distance = [10000]*18

    for id, l in enumerate(light[18:]):

        local = np.array(light[id:id+18])
        distance.append(np.sum((local-median_curve)**2))


    distance = 100*(distance-np.amin(distance))/(np.amax(distance)-np.amin(distance))

    ids = np.where(distance<10)[0]
    print(ids)




    plt.plot(range(len(light)),distance)
    plt.plot(range(len(light)),light)

    #plt.plot(ids,light[ids],'ro')
    plt.plot(ids,distance[ids],'ro')
    plt.show()"""
