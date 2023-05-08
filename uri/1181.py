# exercicio adaptado

import random

while True:
    linha = int(input("num linha "))
    if 0 <= linha <= 11:
        break

ordem = int(input("ordem matriz "))

t = input("soma ou media (S/M) ").upper()

matriz = []

for i in range(ordem):
    linhaN = []
    for j in range(ordem):
        linhaN.append(random.randint(0,20))
    matriz.append(linhaN)

soma = 0

print(matriz)

for i in range(ordem):
    soma += matriz[linha][i]

if t == "S":
    print(f'a soma é {soma}')
elif t == "M":
    print(f'a media é {(soma/ordem):.1f}')

print(matriz[linha])
