import numpy as np

fabric = np.zeros((1000,1000))

for line in open('input.txt'):
    parts = line.split(' ')
    left, top = map(int, parts[2][:-1].split(","))
    width, height = map(int, parts[3].split('x'))
    fabric[left:left+width, top:top+height] += 1

#part 1
#print(np.sum(fabric > 1))




