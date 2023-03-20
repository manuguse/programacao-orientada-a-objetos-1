#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

somaPar = 0
somaImpar = 0

for i in range (10):
    numero = int(input('numero '))
    if(numero%2 == 0):
        somaPar += 1
    else:
        if(numero%2 != 0):
            somaImpar += 1
            
print (f'números pares = {somaPar}')
print (f'números impares = {somaImpar}')
