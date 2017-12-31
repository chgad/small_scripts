import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

# used for uebung 7 Festkoerper 1 VL


k_b = 1.38e-23
G_2 = (2*np.pi*8/(0.4e-9))**2
M = 0.068/(6e23)

plt.xlabel("Temperature [K]")
plt.ylabel("Intensity")


#exponential fit function
def fit_function(T,b):
    return 0.31*np.exp(-(k_b*G_2/(M*b**2)*T))

#linear fit function
def fit_lin(T,b,c):
    return -(k_b*G_2/(M*b**2))*T + c

# Temperature
t = np.array([0, 100, 200, 300, 400, 500])
# Intensities
I = np.array([0.31, 0.22, 0.16,0.1,0.06,0.03])
# ln of I/I_0
I_ln = [np.log(i/0.31) for i in I] 
b0 = np.array([20e12])

data = [(0,0.31),
        (100,0.22),
        (200,0.16),
        (300,0.1),
        (400,0.06),
        (500,0.03)
        ]
# plot data points and linear intrapolation
plt.plot(t, I, label="data, linear intrapolated")
plt.plot(t, I, 'or', label="data, points")

# fit exponentialy
fitParams, fitCo = curve_fit(fit_function,t ,I, b0 )
# fit linear
linfit_Params , fitCO = curve_fit(fit_lin,t,I_ln)
# print the fitted parameters
print(fitParams)
print(linfit_Params)

# calculate first w by hand
plt.plot(t,fit_function(t,20e13), label="guessed with 20 THz")

# plot lin fit of ln()
plt.plot(t,fit_lin(t,linfit_Params[0], linfit_Params[1]),
        label=r"fitted $ln(\frac{I_{h00}}{I_0})$,"+ " w = {:.8} THz".format(linfit_Params[0]/1e12))

# plot exo fit
plt.plot(t, fit_function(t, fitParams[0]),
        label=" calculated w={:.3}THz".format(fitParams[0]/1e12))

plt.legend(loc="best")

plt.show()
