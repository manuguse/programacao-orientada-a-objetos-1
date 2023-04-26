"""Faça um programa que leia uma série de números inteiros e os armazene em uma lista.
O programa deve mostrar a relação de todos os números repetidos. Se não houverem números
repetidos, imprimir uma mensagem avisando que não existem números repetidos nesta lista."""

def verificaNum():
    while True:
        n = int(input(''))
        if n > 1:
            break
    return n

n = int(verificaNum())
numeros = []
repetidos = []

for i in range(n):
    numeros.append(int(input(f'numero {i+1} ')))
    for j in range(len(numeros)):
        if i != j and numeros[i] == numeros[j]:
            repetidos.append(numeros[i])

if len(repetidos) == 0:
    print('nao existem repetidos')
else:
    print(repetidos)
