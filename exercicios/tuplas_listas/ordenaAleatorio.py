"""Crie um programa que gere 5 números aleatórios e os insira em uma tupla.
Mostre a listagem dos números gerados, e indique o maior e o menor.
Você deve implementar a lógica de ordenação"""

import random

x = 0
y = 20
maior = x
menor = y

tupla = (random.randint(x,y), random.randint(x,y), random.randint(x,y), random.randint(x,y), random.randint(x,y))

for i in range(5):
    if tupla[i] > maior:
        maior = tupla[i]
    if tupla[i] < menor:
        menor = tupla[i]
      
print('os numeros sao:', end=' ')
for i in tupla:
    print(i, end=", ")
print(f'o maior é {maior} e o menor é {menor}')
