ledger = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        ledger.append(line)

for i,x in enumerate(ledger):
    for y in ledger[i+1:]:
        diff = 0
        for count,val in enumerate(x):
            if val != y[count]:
                diff += 1
        if diff == 1:
            ans = [val for count, val in enumerate(x) if y[count] == val]
            print(''.join(ans))