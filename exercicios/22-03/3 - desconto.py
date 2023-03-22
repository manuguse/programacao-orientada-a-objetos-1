def calculaDesconto():
    sal = float(input('inserir salário '))
    desconto = float(0.11*sal)
    if (desconto > 320):
        desconto = 320
    print('{:.2f}'.format(desconto))

calculaDesconto()
continua = input('deseja continuar? ').upper()

while (continua != 'S') and (continua != 'N'):
    continua = input('deseja continuar? ').upper()
while (continua == 'S'):
    calculaDesconto()
    continua = input('deseja continuar? ').upper()
while (continua == 'N'):
    break
