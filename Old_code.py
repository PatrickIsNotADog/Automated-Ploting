import matplotlib.pyplot as plt
import numpy as np

#input raw data
data1 = np.loadtxt('./path/data1.txt')
data2 = np.loadtxt('./path/data2.txt')
data3 = np.loadtxt('./path/data3.txt')
data4 = np.loadtxt('./path/data4.txt')

#data1 plot
plt.plot(data1[:,0], data1[:,1],color="r",linestyle="--",linewidth=0.1)
plt.xlabel('Wavelength / nm')
plt.ylabel('Cross section σ / $\mathregular{cm^2}$')
plt.yscale('log')
plt.title('data1')

plt.show()

#data2 plot
plt.plot(data2[:,0], data2[:,1],color="y",linestyle="-",linewidth=0.2)
plt.xlabel('Wavelength / nm')
plt.ylabel('Cross section σ / $\mathregular{cm^2}$')
plt.yscale('log')
plt.title('data2')

plt.show()

#data3 plot
plt.plot(data3[:,0], data3[:,1],color="g",linestyle="-.",linewidth=0.1)
plt.xlabel('Wavelength / nm')
plt.ylabel('Cross section σ / $\mathregular{cm^2}$')
plt.yscale('log')
plt.title('data3')

plt.show()

#data4 plot
plt.plot(data4[:,0], data4[:,1],color="b",linestyle=":",linewidth=0.1)
plt.xlabel('Wavelength / nm')
plt.ylabel('Cross section σ / $\mathregular{cm^2}$')
plt.yscale('log')
plt.title('data4')

plt.show()
