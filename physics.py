"""Core heat-transfer relations used across the project."""
import numpy as np

SIGMA = 5.67e-8  # Stefan-Boltzmann constant, W/m2K4


def conduction(k, A, dT, dx):
    return k * A * dT / dx


def convection(h, A, Ts, Tf):
    return h * A * (Ts - Tf)


def radiation(e, A, Ts, Tsurr):
    """Temperatures in Kelvin."""
    return e * SIGMA * A * (Ts**4 - Tsurr**4)


def lmtd(dT1, dT2):
    dT1, dT2 = max(dT1, 0.1), max(dT2, 0.1)
    if abs(dT1 - dT2) < 1e-9:
        return dT1
    return (dT1 - dT2) / np.log(dT1 / dT2)


def heat_duty(U, A, LMTD):
    return U * A * LMTD
