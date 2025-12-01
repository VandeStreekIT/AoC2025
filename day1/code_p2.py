# Read file
filename = "day1/input_p1.txt"

with open(filename) as f:
    content = f.read().splitlines()

# Attribes

p = 50 # pointer
c = 0 # counter

# Method

def newPointerPosition(p, instruction):
    if instruction[0] == "L":
        mult = abs((p - int(instruction[1:])) // 100)
        remain = (p - int(instruction[1:])) % 100 
        if p == 0:
            mult = mult - 1
        if remain == 0:
            mult = mult + 1
        newP = remain

    elif instruction[0] == "R":
        mult = (p + int(instruction[1:])) // 100
        newP = (p + int(instruction[1:])) % 100 

    return newP, mult

for instruction in content:
    newP, mult = newPointerPosition(p, instruction)
    c = c + mult
    p = newP

print(c)