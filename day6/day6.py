with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

input = [int(n) for n in input[0] if n != ',']

def simulate_day(input):
    new_input = []
    new_lanternfish = 8
    for item in input:
        if item == 0:
            item = 6
            new_input.append(item) 
            new_input.append(new_lanternfish)
        else:
            item -=1
            new_input.append(item)
    return new_input

for day in range(80):
    input = simulate_day(input)

print(len(input))