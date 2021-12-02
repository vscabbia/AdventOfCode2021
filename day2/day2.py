with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

forward = []
up = []
down = []

for item in input:
    if 'forward' in item:
        forward.append(int(item.split()[1]))
    if 'up' in item:
        up.append(int(item.split()[1]))
    if 'down' in item:
        down.append(int(item.split()[1]))

depth = sum(down)-sum(up)

print('Forward:',sum(forward))
print('Up:',sum(up))
print('Down:',sum(down))
print('Depth:', depth)
print('Position:',depth * sum(forward))