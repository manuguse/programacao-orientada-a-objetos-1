# Crie um programa que leia n números inteiros pelo teclado. No final da execução, 
# mostre a média entre os números lidos, qual foi o maior, e o menor valor lido.

n = int(input('insira a quantidade de números '))
somaNumeros = 0

for i in range(n):
    numero = int(input('número '))
    somaNumeros += numero
    
    if (i == 0):
        maiorNumero = numero
        menorNumero = numero
    elif (numero > maiorNumero):
        maiorNumero = numero
    elif (numero < menorNumero):
        menorNumero = numero
    
media = somaNumeros/n
print(f'média = {media}')
print(f'menor número = {menorNumero}')
print(f'maior número = {maiorNumero}')
