from scipy.integrate import quad
from scipy.optimize import curve_fit

from numpy import exp, array
import numpy as np
import matplotlib.pyplot as plt


# This script was used for a Homework for the Festkörper I class
# We got the data T,r provide later and had to calculate the Debey Temperature
# I calculated this with usage of curve_fit and quad in addition with
# the np.vectorize function


def integrand(x):
    return x**5/(( exp(x) - 1)*(1- exp(-x) ))

np.vectorize(integrand)

def INTEGRAL(ratio):
    return quad(integrand, 0.0, ratio)[0]

def rho(T, t_db):
    ratio = t_db/T
    inte = np.vectorize(INTEGRAL)
    return 4.225 *(T/t_db)**5 * inte(ratio)

T = array([4, 10, 30, 50, 70, 100, 150, 200, 250, 300])
r = array([2.27, 2.2702, 2.3057, 2.417, 2.55,
    2.748, 3.063, 3.336, 3.663, 3.956])


# print(quad(exp, 0, 3))
fig, (ax1,ax2, ax3) = plt.subplots(1,3)
# Plot Messpunkte
ax1.plot(T, r, 'or', label="Messpunkte")
ax1.plot(T, r, label="Messpunkte linear intrapoliert")

# Fit

# we substract the rest Resistance at T=0
r = array([t - r[0] for t in r])

ax1.plot(T, r,'or' , label="Messpunktfit ohne Restwiderstand")
params , fitCO = curve_fit(rho, T, r)

# Plot Guess
ax1.plot(T, rho(T, 300), label="Geratener fit mit $ \Theta_{DB}=300} $")

# Plot Fit
ax1.plot(T, rho(T, params[0]), 
        label=r"Fit ergibt $\Theta_{DB}=$ " +"{:.4}".format(params[0]))

ax1.legend(loc="best")

# Nr1 b)
data = [(15, 2.27, 184),
        (30, 1.39, 170),
        (50, 1.17, 174),
        (100, 1.15, 174),
        (200, 0.37, 187)]
T = np.arange(0,300,0.1)

for d , r, t_db in data:
    ax2.plot(T, rho(T, t_db),
        label=r"$\rho(T)$ at $\Theta_{DB} =$"+"{}K".format(t_db))


ax2.legend(loc="best")

# Plot Diamater to Resistance

d = array([f[0] for f in data])
r = array([f[1] for f in data])

ax3.plot(d,r, label=r"$\rho(d)$")

plt.show()

