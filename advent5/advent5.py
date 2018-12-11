data = open('input.txt').read().strip()

def react(polymer):
    length = len(polymer)
    oldLength = None
    while length != oldLength: # If length is unchanged after a pass, we are done. 
        oldLength = length # Now the old length is set
        for each in 'abcdefghijklmnopqrstuvwxyz': # do our replacements
            polymer = polymer.replace(each+each.upper(),"") 
            polymer = polymer.replace(each.upper()+each,"")
            length = len(polymer) # Length is set after replacements
    print(length)

react(data)