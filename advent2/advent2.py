ledger = []
count2 = 0
count3 = 0
import re

with open('input.txt', 'r') as f:
    for line in f.readlines():
        ledger.append(line.strip('\n'))
        
for barcode in ledger:
    for letter in barcode:
        if len(re.findall(letter, barcode)) == 3:
            count3 += 1
            barcode = re.sub(letter,'',barcode)

        
        


