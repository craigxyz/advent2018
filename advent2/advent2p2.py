ledger = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        ledger.append(line.strip('\n'))

def compareStrings(s1,s2):
    built = ''
    for letter in s1:
            if s2[s1.index(letter)] == letter:
                built = built + s1[0:1]
                s1 = s1[1:]
                s2 = s2[1:]
    if len(s1) == 1:
        print(built)

for barcode in ledger:
    for barcode2 in ledger:
        if barcode != barcode2:
            compareStrings(barcode,barcode2)

            

