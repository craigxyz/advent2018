total = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        operation = line[:1]
        num = int(line[1:])

        if operation == '+':
            total += num
        if operation == '-':
            total -= num

print(total)