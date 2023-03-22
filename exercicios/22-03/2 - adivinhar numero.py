from random import randrange

num = randrange(10)
cont = 1
tent = int(input('insira sua tentativa '))

while (num != tent):
    tent = int(input('tente novamente '))
    cont += 1
print('você conseguiu!\no seu número de tentativas foi {}'.format(cont))
