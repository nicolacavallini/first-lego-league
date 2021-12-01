import matplotlib.pyplot as plt
import numpy as np

light = np.array([51, 51, 51, 51, 51, 50, 52, 52, 52, 52, 53, 54, 53, 55, 56, 59, 57, 54, 55, 55, 56, 56, 58, 57, 57, 57, 59, 60, 60, 61, 99, 99, 99, 93, 49, 17, 34, 49, 56, 99, 99, 99, 81, 63, 60, 60, 59, 58, 57, 57, 57, 57, 58, 61, 61, 61, 62, 60, 57, 56, 63, 99, 99, 99, 99, 60, 47, 22, 18, 31, 63, 79, 99, 99, 99, 93, 71, 58, 60, 62, 61, 57, 58, 55, 54, 50, 46, 46, 45, 44, 43, 44, 45, 45, 46, 49, 51, 51, 52, 52, 51, 50, 49, 48, 51, 53, 51, 52, 68, 75, 99, 99, 99, 99, 38, 22, 64, 65, 99, 99, 99, 99, 85, 54, 53, 53, 54, 57, 60, 58, 55, 56, 55, 54, 53, 54, 54, 57, 59, 54, 55, 55, 54, 52, 52, 51, 43, 35, 32, 30, 36, 52, 59, 59, 76, 76, 74, 74, 74, 72, 75, 76, 75, 75, 88, 99, 99, 99, 99, 65, 32, 31, 23, 94, 99, 99, 99, 77, 73, 73])

avanti = light[1:]
indietro = light[0:-1]

pendenza = avanti-indietro

#for l in light[2:]:
#    print(l)

l_min = 50
l_max = 50

corva_mem = []
max_ = []
min_ = []

maschera = [99,99,99,20,20,20,99,99,99]

for i in [18]:#range(9,len(light)):

    curva = 0

    for k in range(9):
        print(k)
        print(i)





"""
for light_map in light:

    if light_map > l_max:
        l_max = light_map

    if light_map < l_min:
        l_min = light_map

    curva = l_max-l_min
    corva_mem.append(curva)

    max_.append(l_max)
    min_.append(l_min)

    if curva > 80:
        l_min = 50
        l_max = 50
"""







#fig, ax = plt.subplots(3,1)
#ax[0].plot(light,'-o')
#ax[1].plot(pendenza,'-o')
#ax[2].plot(corva_mem,'-o')
#ax[2].plot(80*np.ones(np.array(corva_mem).shape),'-g')
#plt.show()
