data = open('input.txt').read().strip()

def p1(polymer):
    length = len(polymer)
    oldLength = None
    while length != oldLength: # If length is unchanged after a pass, we are done. 
        oldLength = length # Now the old length is set
        for each in 'abcdefghijklmnopqrstuvwxyz': # do our replacements
            polymer = polymer.replace(each+each.upper(),"") 
            polymer = polymer.replace(each.upper()+each,"")
            length = len(polymer) # Length is set after replacements
    return(length)
#print(p1(data))

def p2(polymer):
    oPolymer = polymer
    best = 1000000
    for each in 'abcdefghijklmnopqrstuvwxyz':
        polymer = oPolymer
        polymer = polymer.replace(each,"")
        polymer = polymer.replace(each.upper(),"")
        reactedLen = p1(polymer)
        if reactedLen < best:
            best = reactedLen
            print("New best is " + str(best) + " after -" + str(each) + "- replacement")
    return(best)

print(p2(data))