current = 0
history = []
repeated = False

while (repeated == False):
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            operation = line[:1]
            change = int(line[1:])

            if operation == '+':
                current += change
            if operation == '-':
                current -= change

            if current in history:
                repeated = True
                print("Got a hit at " + str(current))
                break
            else:
                history.append(current)

#print(current)