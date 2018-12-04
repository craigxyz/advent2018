count2 = 0
count3 = 0

ledger = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        ledger.append(line.strip('\n'))

for barcode in ledger:
    dicto = {}
    for letter in barcode:
        if letter not in dicto:
            dicto[letter] = barcode.count(letter)
    if 2 in dicto.values():
        count2 += 1
    if 3 in dicto.values():
        count3 += 1

print(count2*count3)