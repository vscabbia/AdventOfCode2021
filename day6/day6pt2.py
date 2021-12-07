import collections
from collections import Counter

with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

input = [int(n) for n in input[0] if n != ',']

input = dict(Counter(input))

input.update({0:0,6:0,7:0,8:0})
aux = 0

new_dict = {}

input = collections.OrderedDict(sorted(input.items()))

for days in range(256):
    parents = input[0]
    for key in range(8):
        valor_atual = input[key]
        if(key != 8):
            novo_valor = input[key+1]  
            input[key] = novo_valor
    input[8] = parents
    input[6] += parents
    
        
print(sum(input.values()))
