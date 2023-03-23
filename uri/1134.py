# exercício 1134

somaAlcool = 0
somaGas = 0
somaDiesel = 0

while True:
    preferido = int(input('item preferido: '))
    if (preferido < 1) or (preferido > 4):
        print('valor inválido')
    elif (preferido == 1):
        somaAlcool += 1
    elif (preferido == 2):
        somaGas += 1
    elif (preferido == 3):
        somaDiesel += 1
    elif (preferido == 4):
        break
    
print('MUITO OBRIGADO')
print(f'Alcool = {somaAlcool}')
print(f'Gasolina = {somaGas}')
print(f'Diesel = {somaDiesel}')
