import numpy as np
from matplotlib import pyplot
# used for uebung 7 Festkoerper 1 VL

k_b = 1.38e-23
G_2 = (2*np.pi/(0.4e-9))**2
M = 0.068/(6e23)
print(G_2)
print(k_b*G_2/M)

def fit_function(T,b,l):
    return 0.31*np.exp(-(k_b*G_2*l**2/(M*b**2)*T))

T = np.linspace(0,500, 10000)

l_s = [1,2,4]
pyplot.xlabel("Temperature [K]")
pyplot.ylabel(r"Intensity $I_{l00}$")


for i in l_s:
    pyplot.plot(T, fit_function(T,22.5e12,i), label=" l={}".format(i))

pyplot.legend(loc="best")
pyplot.show()


