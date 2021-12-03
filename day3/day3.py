import pandas as pd

with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

df = pd.DataFrame({"entrada" : input})

df = df['entrada'].str.split('',expand=True)

answer1 = ''
answer2 = ''

for column in df:
    most_common = df[column].value_counts().index[0]
    least_common = df[column].value_counts().index[-1]
    answer1 += most_common
    answer2 += least_common

answer1=int(answer1, 2)
answer2=int(answer2, 2)


print(answer1 * answer2)
