# Read file
filename = "day1/input_p1.txt"

with open(filename) as f:
    content = f.read().splitlines()

# Attribes

p = 50 # pointer
c = 0 # counter

# Method

def newPointerPosition(p, instruction):
    iDir = instruction[0]
    iSteps = int(instruction[1:])

    if iDir == "L":
        mult = abs((p - iSteps) // 100)
        newP = (p - iSteps) % 100 
        if p == 0:
            mult = mult - 1
        if newP == 0:
            mult = mult + 1

    elif iDir == "R":
        mult = (p + iSteps) // 100
        newP = (p + iSteps) % 100 

    return newP, mult

for instruction in content:
    newP, mult = newPointerPosition(p, instruction)
    c = c + mult
    p = newP

print(c)