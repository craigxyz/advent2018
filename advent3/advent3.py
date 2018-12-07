import numpy as np

claims = []
fabric = np.zeros((1000,1000))

def parse_claims():
    for line in open('input.txt'):
        parts = line.split(' ')
        id = parts[0]
        x, y = map(int, parts[2][:-1].split(","))
        dx, dy = map(int, parts[3].split('x'))
        claims.append([id,x,y,dx,dy])

def p1():
    for (id,x,y,dx,dy) in claims:
        fabric[x:x+dx, y:y+dy] += 1
    return(np.sum(fabric > 1))

def p2():
    for (id,x,y,dx,dy) in claims:
        if np.all(fabric[x:x+dx, y:y+dy] == 1):
            return id

parse_claims()
print(p1())
print(p2())

