""""
Faça um programa que tenha uma função chamada contador(), que tenha 3 parâmetros: inicio, fim e passo, e realize a contagem.
Seu programa terá que realizar 3 contagens através da função criada.

1. a) 1 a 10 de 1 em 1
2. b) 10 a 0 de 2 em 2
3. c) uma contagem personalizada
""""

def contador(x, y, z):
    if x < y:
        for i in range (x,y+1,z):
            print(i, end = ' ')
    elif x > y:
        for i in range (y,x+1,z):
            print(i, end = ' ')
    print()

contador(1,10,1)
contador(10,0,2)
contador(-3,11,4)
