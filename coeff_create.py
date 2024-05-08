from scipy.integrate import quad
import numpy as np
import pandas as pd
from contour import create_contour

settings = open("settings.txt").read()

L = float(settings.split(sep="\n")[0].split(sep="=")[1])
n_degree = int(settings.split(sep="\n")[1].split(sep="=")[1])
name = settings.split(sep="\n")[2].split(sep="=")[1].replace(" ", "")

c_x,c_y =create_contour(name)
t = np.linspace(start=-L, stop=L, num=len(c_x))

f_t = {t[i]: c_x[i] + 1j*c_y[i] for i in range(len(t))}

def continius_izer_3000(d: dict, time:float)-> complex:
    time_line = list(d.keys()).copy()

    lower_bound = None
    upper_bound = None

    for value in time_line:
        if value <= time:
            lower_bound = value
        if value >= time:
            upper_bound = value
            break
    
    if upper_bound - lower_bound == 0:
        return d[lower_bound]
    else:
        m = (time - lower_bound) / (upper_bound - lower_bound)
        return d[lower_bound] + m * (d[upper_bound] - d[lower_bound])
    

def f(t:float) -> complex:
    return continius_izer_3000(f_t,t)


def c_n(L: float, n:int) -> complex:
    aux = n * np.pi/L
    front = 1/(2*L)
    rcos_int = quad(lambda t: np.real(f(t)) * np.cos(t*aux), -L,L, limit=100)[0]
    isin_int = quad(lambda t: np.imag(f(t)) * np.sin(t*aux), -L,L, limit=100)[0]
    icos_int = quad(lambda t: np.imag(f(t)) * np.cos(t*aux), -L,L, limit=100)[0]
    rsin_int = quad(lambda t: np.real(f(t)) * np.sin(t*aux), -L,L, limit=100)[0]

    return front * ( (rcos_int + isin_int) + 1j* (icos_int - rsin_int))



coeffs = [[i,c_n(L=L, n=i)] for i in range(-n_degree, n_degree+1)]
pd.DataFrame(coeffs, columns=["n","c_n"]).to_csv("coefficients_" + str(n_degree) + ".csv", index=False)