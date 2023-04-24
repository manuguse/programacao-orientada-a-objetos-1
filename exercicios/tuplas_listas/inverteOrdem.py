"""Faça um programa que leia uma lista X[0..19] e, após sua criação, troque a posição
do 1º elemento pela posição do 20º elemento, o 2º com o 19º e assim por diante. Ao final, imprima X."""

num = 19
x = []
for i in range(20):
    x.append(i)
print(x)

y = x[:]
for i in range(num+1):
    x[num-i] = y[i]

print(x)
