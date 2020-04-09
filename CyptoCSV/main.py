import fileinput
from matplotlib import pyplot as plt

file = fileinput.input("BTC-1Hr.csv")

introduction = file.readline()

i = 0
for line in file:
    line = line.strip().split(',')
    
    print(line)
    day = int(line[0][8:10])
    
    if day ==
    i += 1
    if i >= 20:
        break

file.close()

plt.plot([1, 2, 3], [4, 5, 1])
plt.show()