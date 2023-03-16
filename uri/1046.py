# exercício 1046

x = int(input('horário inicio '))
while (x>24) or (x<0):
    print('valor inválido')
    x = int(input('inicio '))

y = int(input('horário fim '))
while (y>24) or (y<0):
    print('valor inválido')
    y = int(input('horário fim '))
    
if (y > x):
    duracao = y-x
    print(f'O JOGO DUROU {duracao} HORA(S)')

elif (x > y):
    duracao = 24 - x + y
    print(f'O JOGO DUROU {duracao} HORA(S)')

else:
    print('O JOGO DUROU 24 HORA(S)')
