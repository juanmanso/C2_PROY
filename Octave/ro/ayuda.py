import matplotlib.pyplot as plt
import csv
import numpy as np
import math

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Computer Modern']})
rc('text', usetex=True)

## Grafico de regulacion de carga
f = []
ro = []
with open('data_ro.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        f.append(float(row[0]))
        ro.append(float(row[1]))

plt.figure()
plt.title("Impedancia de salida", fontsize=18)
plt.xlabel(r"Resistencia de carga [$\Omega$]")
plt.ylabel(r"$R_o$ [\Omega]")
plt.semilogx(f,ro, linestyle='-', marker='o')
#plt.xlim(200,0)
plt.grid()

plt.savefig('med_zo.pdf')
########################################

