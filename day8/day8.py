with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

x = [item.split('|') for item in input]

input = [item.split(' ') for item in input]

num1 = num4 = num7= num8 = 0

for item in range(len(input)):
    for i in range(11,15):
        code_size = len(input[item][i])
        if code_size == 2:
            num1 += 1
        elif code_size == 4:
            num4 += 1
        elif code_size == 3:
            num7 += 1
        elif code_size == 7:
            num8 += 1

lista = [num1,num4,num7,num8]
print(sum(lista))