with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

input = map(int, input)

def classify(item):
    if item.entrada > item.entrada_anterior:
        return 'Increase'
    elif item.entrada < item.entrada_anterior:
        return 'Decrease'
    elif item.entrada == item.entrada_anterior:
        return 'Equal'
    else:
        return 'First'


import pandas as pd

df = pd.DataFrame({"entrada" : input})

df['entrada_anterior']=df.shift(periods=1)
df['result'] = df.apply(lambda x: classify(x),axis=1)
print(df['result'].value_counts())
