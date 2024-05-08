import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from contour import create_contour


settings = open("settings.txt").read()

L = float(settings.split(sep="\n")[0].split(sep="=")[1])
n_degree = int(settings.split(sep="\n")[1].split(sep="=")[1])
name = settings.split(sep="\n")[2].split(sep="=")[1].replace(" ", "")

c_x,c_y =create_contour(name)
t = np.linspace(start=-L, stop=L, num=len(c_x))


def sum_at_t(t: float, c:np.array) -> complex:
    cum = 0
    for n in range(-n_degree, n_degree+1):
        aux = n * np.pi/L
        cum += c[n] * (np.cos(aux*t) + 1j*np.sin(aux*t))
    
    return cum


coeffs = pd.read_csv("coefficients_" + str(n_degree) + ".csv", index_col="n")
coeffs["c_n"] = coeffs["c_n"].apply(lambda c: complex(c))

coeffs_dict = coeffs.to_dict()["c_n"]


df = pd.DataFrame()
df["t"] = np.linspace(start=-L, stop=L, num=1000)
df["f(t)"] = df["t"].apply(lambda t: sum_at_t(t, coeffs_dict))


sns.set_theme()

figure, axis = plt.subplots(2, 2)
figure.set_figheight(10)
figure.set_figwidth(10)

axis[0, 0].plot(t, c_x) 
axis[0, 0].set_title("Real og") 

axis[0, 1].plot(t, c_y) 
axis[0, 1].set_title("Imag og") 

axis[1, 0].plot(df["t"], df["f(t)"].apply(lambda i: np.real(i))) 
axis[1, 0].set_title("Real fourier") 

axis[1, 1].plot(df["t"], df["f(t)"].apply(lambda i: np.imag(i))) 
axis[1, 1].set_title("Imag fourier") 

plt.show()


figure_2, axis_2 = plt.subplots(1, 2) 
figure_2.set_figheight(6)
figure_2.set_figwidth(12)

axis_2[0].plot(c_x, c_y) 
axis_2[0].set_title("Og") 


axis_2[1].plot(df["f(t)"].apply(lambda f: np.real(f)), df["f(t)"].apply(lambda f: np.imag(f)))
axis_2[1].set_title("fourier") 

plt.show()