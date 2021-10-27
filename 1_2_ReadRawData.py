import codecs

# Step 1 - Read Dark BG & Noise
# Read Dark BG
# Open file and read in 'utf-8' encoding
Dark_BG = codecs.open('./RawData/Dark_BG_Noise.txt', mode='r', encoding='utf-8')
# Read as a line
line = Dark_BG.readline()
list_Dark_BG = []
while line:
    a = line.split()
    # Number of lines to be read
    b = a[1:2]
    # Add to the list_Dark_BG
    list_Dark_BG.append(b)
    line = Dark_BG.readline()
Dark_BG.close()

# Read Dark Noise
# Open file and read in 'utf-8' encoding
Dark_Noise = codecs.open('./RawData/Dark_BG_Noise.txt', mode='r', encoding='utf-8')
# Read as a line
line = Dark_Noise.readline()
list_Dark_Noise = []
while line:
    a = line.split()
    # Number of lines to be read
    b = a[2:3]
    # Add to the list_Dark_BG
    list_Dark_Noise.append(b)
    line = Dark_Noise.readline()
Dark_Noise.close()

# Step 2 - Read Sample & BG
# Read Sample1
Sample1 = codecs.open('./RawData/Sample.txt', mode='r', encoding='utf-8')
# Read as a line
line = Sample1.readline()
list_Sample1 = []
while line:
    a = line.split()
    # Number of lines to be read
    b = a[1:2]
    # Add to the list_Dark_BG
    list_Sample1.append(b)
    line = Sample1.readline()
Sample1.close()

# Read BG1
BG1 = codecs.open('./RawData/BG.txt', mode='r', encoding='utf-8')
# Read as a line
line = BG1.readline()
list_BG1 = []
while line:
    a = line.split()
    # Number of lines to be read
    b = a[1:2]
    # Add to the list_Dark_BG
    list_BG1.append(b)
    line = BG1.readline()
BG1.close()

# Output Test
#for i in list_Dark_BG:
#    print(i)
