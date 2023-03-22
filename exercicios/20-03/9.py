# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual número ele deseja ver a tabuada.

num = int(input('tabuada do número '))

for i in range (1, 11):
    resultado = num*i
    print(f'{num} X {i} = {resultado}')
