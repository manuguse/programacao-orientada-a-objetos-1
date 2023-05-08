# exercicio adaptado

import random

ordem = int(input("ordem matriz "))
opcao = input("deseja preencher pelo teclado ou de forma randomica? (T/R) ").upper()
t = input("soma ou media (S/M) ").upper()

# cria matriz 
matriz = []

for i in range(ordem):
    linhaN = []
    if opcao == 'T':
        linhaN = (input().split(" "))
    else:
        for j in range(ordem):
            linhaN.append(random.randint(0,10))
    matriz.append(linhaN)

# opera matriz
soma = 0
contador = 0

for i in range(ordem):
    for j in range(i):
        soma += matriz[i][j]
        contador += 1

if t == "S":
    print(soma)
if t == "M":
    print(soma/contador)

print(matriz)
