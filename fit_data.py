import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

k_b = 1.38e-23
G_2 = (2*np.pi*8/(0.4e-9))**2
M = 0.068/(6e23)
print(G_2)
print(k_b*G_2/M)

def fit_function(T,b):
    return 0.31*np.exp(-(k_b*G_2/(M*b**2)*T))
t = np.array([0, 100, 200, 300, 400, 500])
I = np.array([0.31, 0.22, 0.16,0.1,0.06,0.03])
b0 = np.array([20e12])
data = [(0,0.31),
        (100,0.22),
        (200,0.16),
        (300,0.1),
        (400,0.06),
        (500,0.03)
        ]

zipped = zip(*data)
plt.scatter(*zipped)

plt.plot(t, I)
plt.plot(t, I, 'or')
fitParams, fitCo = curve_fit(fit_function,t ,I, b0 )

print(fitParams)
plt.plot(t,fit_function(t,20e13), label="guessed wit 20 THz")
plt.plot(t, fit_function(t, fitParams[0]), label=" calculated w={:.3}THz".format(fitParams[0]/1e12))
plt.legend(loc="best")

plt.show()
