# Faça um programa que receba dois números inteiros e gere os números inteiros que 
# estão no intervalo compreendido por eles. No final mostre a soma dos números (do intervalo).

numero1 = int(input('numero 1 '))
numero2 = int(input('numero 2 '))
somaNumero = 0
inicio = 0
fim = 0

if (numero1 < numero2):
    inicio = numero1 + 1
    fim = numero2
    
else:
    inicio = numero2 + 1
    fim = numero1
    
for i in range (inicio, fim):
    somaNumero += i

print(somaNumero)
