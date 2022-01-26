import numpy

import matplotlib.pyplot as plt

from scipy import integrate


def H(z, omega_m, H_0=70):
    omega_lambda = 1 - omega_m
    z_prime = ((1 + z) ** 3)
    wurzel = numpy.sqrt(omega_m * z_prime + omega_lambda)

    return H_0 * wurzel


def H_inv(z, omega_m, H_0=70):
    return 1 / (H(z, omega_m, H_0=70))


def integral(z, omega_m, H_0=70):
    I = integrate.quad(H_inv, 0, z, args=(omega_m,))[0]
    return I


def d_L(z, omega_m, H_0=70):
    distance = (2.99 * (10 ** 8)) * (1 + z) * integral(z, omega_m, H_0)
    return distance

z0 = -1.8
zf = 10
zs = numpy.linspace(z0, zf, 1000)
d_Ls = numpy.linspace(z0, zf, 1000)
omega_m = 0.2

for index in range(zs.size):
     d_Ls[index] = d_L(zs[index], omega_m=omega_m)
plt.plot(zs,d_Ls)
plt.show()