import numpy as np

with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

def tuple_int_str(tuple_str):
    result = tuple((int(x[0]), int(x[1]),int(x[2]),int(x[3])) for x in tuple_str)
    return result

ajusted_input = []
for item in input:
    item = item.replace(" -> ", ",")
    ajusted_input.append(tuple(item.split(',')))

ajusted_input = tuple_int_str(ajusted_input)

x1, y1, x2, y2 = 0, 1, 2, 3
points = []

for item in ajusted_input:
    maior_x = max(item[x1],item[x2])
    menor_x = min(item[x1],item[x2])
    maior_y = max(item[y1],item[y2])
    menor_y = min(item[y1],item[y2])
    x_diff = maior_x-menor_x
    y_diff = maior_y-menor_y
    if x_diff == 0 and y_diff != 0:
        for item in list(range(menor_y,maior_y+1)):
            points.append([maior_x,item])
    elif y_diff == 0 and x_diff != 0:
        for item in list(range(menor_x,maior_x+1)):
            points.append([item,maior_y])
    else:

        if item[x1] < item[x2]:
            stepx = 1
        else:
            stepx = -1
        if item[y1] < item[y2]:
            stepy = 1
        else:
            stepy = -1
        for item2, item1 in zip(range(item[y1],item[y2]+stepy,stepy),range(item[x1],item[x2]+stepx,stepx)):     
            points.append([item1,item2])

matrix = np.zeros((1000,1000), dtype=int)

for point in points:
    matrix[point[0]][point[1]] +=1

count = 0
for line in matrix:
    for item in line:
        if(item > 1):
         count += 1

print(count)