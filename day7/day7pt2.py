with open('input.txt') as f:
    input = [line.split(',') for line in f]
import math
input = input[0]
input = list(map(int, input))

#Calcular na mão
# def calculate_fuel(num):
#     step_cost = 1
#     fuel = 0
#     for value in range(1,num+1):
#        fuel += step_cost
#        step_cost += 1
#     return fuel

def calculate_fuel(num):
    return int(num*(num+1)/2)


for n in range(min(input),max(input)):
    fuel = 0
    for item in input:
        value_to_n = n - item
        fuel += calculate_fuel(abs(value_to_n))
    if(n == min(input)):
        least_fuel = fuel
    elif(fuel<least_fuel):
        least_fuel = fuel


print(least_fuel)