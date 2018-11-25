import matplotlib.pyplot as plt
import csv
import numpy as np
import math

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Computer Modern']})
rc('text', usetex=True)

## Grafico de etapa de salida a 1kHz con THD=0.154031%
tiempo = []
vo = []
vl1 = []
vl2 = []
with open('datos/1.4_comparador_valores_res.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        tiempo.append(float(row[0])*1e3)
        vl1.append(float(row[1]))
        vl2.append(float(row[2]))
        vo.append(float(row[3]))

plt.figure()
plt.title(r"Simulaci\'on de etapa de salida", fontsize=18)
plt.xlabel(r"Tiempo [$ms$]")
plt.ylabel("Salida $[V]$")
plt.plot(tiempo,vo, tiempo, vl1, tiempo, vl2)
plt.xlim(0,3.1)
plt.gca().legend(('$V_o$', '$V_{L+}$', '$V_{L-}$'))
plt.grid()

plt.savefig('graficos/etapa_salida_simulacion.pdf')


## Grafico de VAS y primera etapa a 1kHz con THD=0.000205%

tiempo =[]
vas = []
with open('datos/2.1_VAS_PD.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        tiempo.append(float(row[0])*1e3)
        vas.append(float(row[1]))

plt.figure()
plt.title(r"Simulacion de VAS", fontsize=18)
plt.xlabel(r"Tiempo [ms]")
plt.ylabel("Salida VAS")
plt.plot(tiempo, vas)
plt.xlim(0,3)
plt.grid()

plt.savefig('graficos/2.1_vas.pdf')


## Bode de VAS con MF=60 C=400p



f = []
ganancia = []
fase = []

with open('datos/vas_bode.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        f.append(float(row[0]))
        ganancia.append(float(row[1]))
        fase.append(float(row[2]))

fig, ax1 = plt.subplots()

color = 'blue'
ax1.set_xlabel('Frecuencia [kHz]')
ax1.set_ylabel('Ganancia [dB]',color=color)
ax1.semilogx(f, ganancia, color=color)
#ax1.set_ylim ([9.23, 9.24])
plt.grid()
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  

color = 'red'
ax2.set_ylabel('Fase', color=color)  
ax2.semilogx(f, fase, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Respuesta en frecuencia de VAS')

plt.savefig('graficos/vas_bode.pdf')

###################################################



