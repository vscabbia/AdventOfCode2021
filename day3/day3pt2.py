import pandas as pd
import numpy
ratings = ['ogr', 'co2']
result_list = []

with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

df_input = pd.DataFrame({"entrada": input})
df_input = df_input['entrada'].str.split('', expand=True)
columns = [0, 13]
df_input.drop(columns, inplace=True, axis=1)

for rating in ratings:
    df = df_input.copy()
    for column in df.columns:
        if df.shape[0] != 1:
            mc_value = df[column].value_counts().values[0]
            lc_value = df[column].value_counts().values[1]
            mc_index = df[column].value_counts().index[0]
            lc_index = df[column].value_counts().index[-1]
            if rating == 'ogr':
                if(int(mc_value) == int(lc_value)):
                    mc_index = "1"
                df = df[df[column] == mc_index]
            if rating == 'co2':
                if(int(mc_value) == int(lc_value)):
                    lc_index = "0"
                df = df[df[column] == lc_index]

    df['result'] = df.apply(''.join, axis=1)
    result = df['result'].values[0]
    integer = int(result, 2)
    result_list.append(integer)
print(numpy.prod(result_list))
