soma_coelho = 0
soma_rato = 0
soma_sapo = 0
soma_cobaia = 0

while True:
    num = int(input('numero de testes '))
    if 1 <= num <= 15:
        break
    
for i in range (num):
    while True:
        cobaia_num, cobaia_esp = input('quantidade de especie ').split(' ')
        cobaia_num = int(cobaia_num)
        if cobaia_num > 0 and (cobaia_esp == 'C' or cobaia_esp == 'R' or cobaia_esp == 'S'):
            break
        elif cobaia_num > 0:
            print('espécie inválida')
        elif cobaia_esp.upper() == 'C' or cobaia_esp.upper() == 'R' or cobaia_esp.upper() == 'S':
            print('valor inválido')
        else:
            print('criterios invalidos')

    soma_cobaia += cobaia_num
    
    if cobaia_esp.upper() == 'C':
        soma_coelho += cobaia_num
    elif cobaia_esp.upper() == 'R':
        soma_rato += cobaia_num
    elif cobaia_esp.upper() == 'S':
        soma_sapo += cobaia_num

print(f'total: {soma_cobaia} cobaias')
print(f'total coelhos: {soma_coelho}')
print(f'total ratos: {soma_rato}')
print(f'total sapos: {soma_sapo}')

print(f'percentual de coelhos: {(soma_coelho/soma_cobaia)*100:.2f} %')
print(f'percentual de ratos: {(soma_rato/soma_cobaia)*100:.2f} %')
print(f'percentual de sapos: {(soma_sapo/soma_cobaia)*100:.2f} %')
