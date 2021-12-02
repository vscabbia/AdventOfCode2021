with open('input2.txt') as f:
    input = [line.rstrip('\n') for line in f]

input = map(int, input)

def classify(item):
    if item.soma > item.soma_anterior:
        return 'Increase'
    elif item.soma < item.soma_anterior:
        return 'Decrease'
    elif item.soma == item.soma_anterior:
        return 'Equal'
    else:
        return 'First'


import pandas as pd

df = pd.DataFrame({"entrada" : input})

df['entrada_anterior']=df.entrada.shift(periods=1)
df['entrada_antes_anterior']=df.entrada.shift(periods=2)
df = df[2:]
df['soma'] = df.sum(axis=1)
df['soma_anterior']=df.soma.shift(periods=1)
df['result'] = df.apply(lambda x: classify(x),axis=1)
print(df['result'].value_counts())
#print(df)