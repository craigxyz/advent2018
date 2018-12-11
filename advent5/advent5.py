data = open('input.txt').read().strip()
length = len(data)
oldLength = length + 1 # See comment below

while length != oldLength: # If length is unchanged after a pass, we are done. 
    oldLength = length # Now the old length is set
    for each in 'abcdefghijklmnopqrstuvwxyz': # do our replacements
        data = data.replace(each+each.upper(),"") 
        data = data.replace(each.upper()+each,"")
        length = len(data) # Length is set after replacements
print(length)
    