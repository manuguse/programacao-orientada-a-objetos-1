""""Desenvolva um programa que contém uma tupla com 5 valores do tipo inteiro. Esses valores devem ser lidos do teclado. Ao final mostre:
  a) quantas vezes apareceu o número 9
  b) em que posição foi digitado o primeiro valor 3
  c) quais foram os números pares digitados""""

def insereValor():
    x = int(input(''))
    return x

def verificaNove():
    somaNove = 0
    for i in range(5):
        if int(tupla[i]) == 9:
            somaNove += 1
    return somaNove

def verificaTres():
    for i in range(5):
        if int(tupla[i]) == 3:
            return i
        
def verificaPar():
    pares = []
    for i in range(5):
        if int(tupla[i]%2) == 0:
            pares.append(tupla[i])
    return pares

tupla = (insereValor(), insereValor(), insereValor(),insereValor(), insereValor())

print(f'o numero 9 aparece {verificaNove()} vez(es)')
print(f'o numero 3 foi digitado pela primeira vez na posição {verificaTres()}')
print(f'os numeros pares sao {verificaPar()}')
