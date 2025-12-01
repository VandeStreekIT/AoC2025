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
        newP = (p - int(instruction[1:])) % 100 
    elif instruction[0] == "R":
        newP = (p + int(instruction[1:])) % 100 
        
    return newP

for instruction in content:
    p = newPointerPosition(p, instruction)
    if p == 0:
        c += 1

print(c)