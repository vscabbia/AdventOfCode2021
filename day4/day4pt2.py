import numpy as np
numbers = [26, 38, 2, 15, 36, 8, 12, 46, 88, 72, 32, 35, 64, 19, 5, 66, 20, 52, 74, 3, 59, 94, 45, 56, 0, 6, 67, 24, 97, 50, 92, 93, 84, 65, 71, 90, 96, 21, 87, 75, 58, 82, 14, 53, 95, 27, 49, 69, 16,
           89, 37, 13, 1, 81, 60, 79, 51, 18, 48, 33, 42, 63, 39, 34, 62, 55, 47, 54, 23, 83, 77, 9, 70, 68, 85, 86, 91, 41, 4, 61, 78, 31, 22, 76, 40, 17, 30, 98, 44, 25, 80, 73, 11, 28, 7, 99, 29, 57, 43, 10]

numbers = [str(n) for n in numbers]


def ler_matriz():
    with open('input.txt') as f:
        input = [line.rstrip('\n') for line in f]

    matrizes = [item.split(' ') for item in input]

    # removing empty strings from lists
    for matriz in matrizes:
        for linha in matrizes:
            try:
                linha.remove("")
            except:
                pass
    matrizes = [x for x in matrizes if x]

    matrizes_ajeitadas = []
    for i in range(0, len(matrizes), 5):
        matriz = matrizes[i:i+5]
        matrizes_ajeitadas.append(matriz)
    return matrizes_ajeitadas


def check_number(value, matriz):
    for linha in matriz:
        try:
            index = linha.index(value)
            linha[index] = 'X'
        except:
            pass


def transpose(matriz):
    transposta = []
    for row_index in range(5):
        for col_index in range(5):
            val = matriz[row_index][col_index]
            if row_index == 0:
                transposta.append([val])
            else:
                transposta[col_index].append(val)
    return transposta


def is_bingo_line(matriz):
    for linha in matriz:
        result = ''. join(linha)
        if result == 'XXXXX':
            return True
    return False


def is_bingo_column(matriz):
    return is_bingo_line(transpose(matriz))


def is_winner(matriz):
    if(is_bingo_line(matriz) or is_bingo_column(matriz)):
        return True


matrizes = ler_matriz()

matriz_bingo = 0
campeao = 0
final_number = 0

flags = [False] * len(matrizes)

for number in numbers:
    if campeao == len(matrizes):
        break
    for i, matriz in enumerate(matrizes):
        check_number(number, matriz)
        if(flags[i] == False and is_winner(matriz)):
            campeao += 1
            matriz_bingo = matriz
            final_number = number
            flags[i] = True


for linha in matriz_bingo:
    for item in linha:
        if(item == 'X'):
            index = linha.index(item)
            linha[index] = 0
        else:
            index = linha.index(item)
            linha[index] = int(item)

matrix_sum = np.sum(matriz_bingo)

result = matrix_sum * int(final_number)

print(result)
