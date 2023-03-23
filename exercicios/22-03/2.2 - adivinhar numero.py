from random import randrange

num = randrange(11)
cont = 1
while True:
    tent = int(input('insira sua tentativa '))
    if (tent > 10) or (tent < 0):
        print('numero inválido')
    elif (num!= tent):
        print('tente novamente')
        cont += 1
    else: break
print('você conseguiu!\no seu número de tentativas foi {}'.format(cont))
