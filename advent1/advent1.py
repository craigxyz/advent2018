current = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        operation = line[:1]
        change = int(line[1:])

        if operation == '+':
            current += change
        if operation == '-':
            current -= change

print(current)