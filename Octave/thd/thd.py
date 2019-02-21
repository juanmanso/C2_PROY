import matplotlib.pyplot as plt
import csv
import numpy as np 
import math

f =[]
thd_01 = []
thd_03 = []
thd_1 = []
thd_3 = []
thd_10 = []
thd_30 = []
thd_40 = []



with open('data.csv', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		f.append(float(row[0]))
		thd_01.append(float(row[1]))
		thd_03.append(float(row[2]))
		thd_1.append(float(row[3]))
		thd_3.append(float(row[4]))
		thd_10.append(float(row[5]))
		thd_30.append(float(row[6]))	
		thd_40.append(float(row[7]))		


plt.figure()
plt.plot(f,thd_01, linestyle='-', marker='o')
plt.plot(f,thd_03, linestyle='-', marker='o')
plt.plot(f,thd_1, linestyle='-', marker='o')
plt.plot(f,thd_3, linestyle='-', marker='o')
plt.plot(f,thd_10, linestyle='-', marker='o')
plt.plot(f,thd_30, linestyle='-', marker='o')
plt.plot(f,thd_40, linestyle='-', marker='o')

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("THD [%]")
plt.grid()
plt.legend(['0,1W', '0,3W', '1W', '3W','10W', '30W', '40W'], loc='upper right')

plt.savefig('thd.pdf')		


## Mismo grafico con zoom
plt.figure()
plt.plot(f,thd_01, linestyle='-', marker='o')
plt.plot(f,thd_03, linestyle='-', marker='o')
plt.plot(f,thd_1, linestyle='-', marker='o')
plt.plot(f,thd_3, linestyle='-', marker='o')
plt.plot(f,thd_10, linestyle='-', marker='o')
plt.plot(f,thd_30, linestyle='-', marker='o')
plt.plot(f,thd_40, linestyle='-', marker='o')
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("THD [%]")
plt.xlim(50, 10000)
plt.ylim(0,0.4)
plt.grid()
plt.legend(['0,1W', '0,3W', '1W', '3W', '10W', '30W', '40W'], loc='upper right')

plt.savefig('thd_zoom.pdf')		