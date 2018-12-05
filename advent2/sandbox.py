ledger = []
prev = ''

with open('input.txt', 'r') as f:
    for line in f.readlines():
        ledger.append(line)

for barcode in ledger:
    for letter in barcode:
        if letter == prev:
            print(barcode)
            print(letter + " is the same as " + prev + " which came before it.")
        else:
            prev = letter


