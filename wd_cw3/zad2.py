import random

macierz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for y in range(0,3):
    for x in range(0,3):
        macierz [y][x] = random.randrange(1, 10)

for y in range(0,3):
    for x in range(0,3):
        print(macierz [y][x],end=',')
    print("")

lista = [macierz[x][x] for x in range(3)]

print(lista)