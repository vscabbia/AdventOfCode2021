with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

horizontal = 0
depth = 0
aim = 0

for item in input:
    if 'forward' in item:
        value = int(item.split()[1])
        horizontal += value
        if aim != 0:
            depth += value * aim        
    if 'up' in item:
        value = int(item.split()[1])
        aim -= value        
    if 'down' in item:
        value = int(item.split()[1])
        aim += value
        
print('horizontal:',horizontal)
print('depth:',depth)
print('answer',horizontal * depth)
