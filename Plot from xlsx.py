import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import os

#Read a single file
#df = np.loadtxt('./path/sample.xlsx')
#x,y = df['x'], df['y']
#fig = plt.figure()
#sub = fig.add_subplot(111)
#sub.plot(x,y)
#plt.show()


#Read multiple files
#use glob to search files
files = sorted(glob('./path/*.xlsx'))
print(files)

#Create a folder to save figures
if not os.path.exists('./path/Folder name'):
    os.mkdir('./path/Folder name')

#Plot
for i in range(len(files)):
    print('Processing File #{:03d}...'.format(i))
    fig = plt.figure()
    sub = fig.add_subplot(111)
    
    df = pd.read_excel(files[i])
    
    x = df['x']
    y = df['y']

    sub.plot(x,y,
             label='{:03d}'.format(i))
             
    #sub.legend()
    sub.set_yscale('log')
    sub.set_xlabel('Wavelength / nm')
    sub.set_ylabel('Cross section σ / $\mathregular{cm^2}$')
    sub.set_title('File #{:03d}'.format(i))
    fig.tight_layout()
    plt.show()
    fig.savefig('./Documents/figure/{:03d}.png'.format(i))
plt.close(fig)
