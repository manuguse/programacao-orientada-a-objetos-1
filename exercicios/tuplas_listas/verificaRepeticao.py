""" Faça um programa que leia uma série de números inteiros e os armazene em uma
lista. Em seguida, o programa deve determinar se nessa série de valores aparece
algum valor repetido. Mostrar mensagem dizendo se existe ou não um número repetido!
O número de elementos é definido pelo usuário. """

num = int(input("qtde "))
inteiros = []
cont = 0

for i in range(num):
    inteiros.append(int(input(f"numero {i+1} ")))

for k in range(num):
    cont += inteiros.count(inteiros[k])

if cont > num:
    print("\nexiste numero repetido")
else:
    print("\nnao existe numero repetido")
        
