# Faça um programa que peça para n pessoas a sua idade (o valor de n será solicitado ao usuário),
# ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n = int(input('numero de pessoas '))
somaIdade = 0

for i in range (n):
    if (i == 0):
        idade = int(input('idade '))
        somaIdade += idade
    else:
        idade = int(input('idade '))
        somaIdade += idade
        
media = somaIdade/n

if (0 < media <= 25):
    print('jovem')
elif (25 < media <= 60):
    print('adulto')
else:
    print('idoso')
