with open('input.txt') as f:
    input = [line.split(',') for line in f]

input = input[0]
input = list(map(int, input))


for n in range(min(input),max(input)):
    fuel = 0
    for item in input:
        value_to_n = n - item
        fuel += abs(value_to_n)

    if(n == min(input)):
        least_fuel = fuel
    elif(fuel<least_fuel):
        least_fuel = fuel

print(least_fuel)
