import matplotlib.pyplot as plt
import csv
import numpy as np
import math

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Computer Modern']})
rc('text', usetex=True)

## Grafico de regulacion de carga
rl = []
vo = []
with open('datos/regulacion_carga.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        rl.append(float(row[0]))
        vo.append(float(row[1]))

plt.figure()
plt.title(r"Regulaci\'on de carga", fontsize=18)
plt.xlabel(r"Resistencia de carga [$\Omega$]")
plt.ylabel("$V_o$ [V]")
plt.plot(rl,vo)
plt.xlim(200,0)
plt.grid()

plt.savefig('graficos/regulacion_carga.pdf')
########################################



## Gráfico de Vo vs. Io
plt.figure()
plt.title(r"Transferencia por simulaci\'on", fontsize=18)
plt.xlabel("$I_o [mA]$")
plt.ylabel("$V_o [V]$")
plt.grid()
plt.plot([1e3*x/y for x,y in zip(vo, rl)], vo)

plt.savefig('graficos/vo_io.pdf')
########################################


## Grafico de regulacion de linea

vi = []
vo = []
with open('datos/regulacion_linea.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        vi.append(float(row[0]))
        vo.append(float(row[1]))
plt.figure()
plt.title(r"Regulaci\'on de l\'inea")
plt.xlabel("$V_i$ [V]")
plt.ylabel("$V_o$ [V]")
plt.plot(vi,vo)
plt.grid()

plt.savefig('graficos/regulacion_linea.pdf')
###########################################




## Grafico de ruido para RL 100 y 50 ohm

f = []
deltav = []
deltav_50 = []
with open('datos/ruido.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        f.append(float(row[0]))
        deltav.append(float(row[1])*1e9)
        deltav_50.append(float(row[2])*1e6)

fig, ax1 = plt.subplots()

color = 'blue'
plt.title("Ruido en la salida")
ax1.set_xlabel("Frecuencia [Hz]")
ax1.set_ylabel("$V_o$ [$\mathrm{nV/\sqrt{Hz}}$], $R_L=100 \Omega$", color=color)
l1=ax1.semilogx(f, deltav, color=color)
plt.grid()
ax1.tick_params(axis='y', labelcolor=color)
#ax1.legend(['$R_L=100 \Omega$'], loc="lower right")

ax2 = ax1.twinx()

color = 'red'
ax2.set_ylabel("$V_o$ [$\mathrm{\mu V/\sqrt{Hz}}$], $R_L=50 \Omega$", color=color)
l2=ax2.semilogx(f, deltav_50, color=color)
ax2.tick_params(axis='y', labelcolor=color)
#ax2.legend(['$R_L=50 \Omega$'], loc="upper right")

plt.savefig('graficos/ruido.pdf')
#######################################


## Grafico de impedancia de salida

t = []
v_sal = []
i_sal = []

with open('datos/zo.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        t.append(float(row[0])*1e3)
        v_sal.append(float(row[1]))
        i_sal.append(float(row[2])*1e3)

fig, ax1 = plt.subplots()

color = 'blue'
ax1.set_xlabel('Tiempo [ms]')
ax1.set_ylabel('$V_{sal}$ [V]',color=color)
ax1.plot(t, v_sal, color=color)
ax1.set_ylim ([9.23, 9.24])
plt.grid()
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  

color = 'red'
ax2.set_ylabel('$I_{sal} [mA]$', color=color)  
ax2.plot(t, i_sal, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Impedancia de salida con $R_L=100 \Omega$')

plt.savefig('graficos/zo.pdf')

###################################################


## Grafico de tension de salida al variar R9

r = []
vo = []
with open('datos/vo_r9.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        r.append(float(row[0])/1e3)
        vo.append(float(row[1]))
plt.figure()
plt.title(r"Variaci\'on de $R_9$")
plt.xlabel("$R_9 [\mathrm{k}\Omega]$")
plt.ylabel("$V_o$ [V]")
plt.plot(r,vo)
plt.grid()

plt.savefig('graficos/vo_r9.pdf')
################################################

## Grafico de corriente de salida

r = []
io = []
with open('datos/io_r18_rl_1.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        r.append(float(row[0])/1e3)
        io.append(float(row[1]))
plt.figure()
plt.title(r"Variaci\'on de $R_{18}$ con $R_L=1 \Omega$ ")
plt.xlabel("$R_{18} [\mathrm{k}\Omega]$")
plt.ylabel("$I_o$ [A]")
plt.plot(r,io)
plt.grid()

plt.savefig('graficos/io_r18.pdf')
###############################################


## Grafico de ripple

t = []
vi = []
vo = []

with open('datos/ripple.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        t.append(float(row[0])*1e3)
        vi.append(float(row[1]))
        vo.append(float(row[2]))

fig, ax1 = plt.subplots()

color = 'blue'
ax1.set_xlabel('Tiempo [ms]')
ax1.set_ylabel('$V_o$ [V]',color=color)
ax1.plot(t, vo, color=color)
plt.grid()
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  

color = 'red'
ax2.set_ylabel('$V_i [V]$', color=color)  
ax2.plot(t, vi, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Factor de rechazo')

plt.savefig('graficos/ripple.pdf')

###################################################





