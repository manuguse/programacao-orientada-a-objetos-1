while True:
    precoAlcool = float(input('preco alcool '))
    if (0.01 <= precoAlcool <= 10):
        break

while True:
    precoGas = float(input('preco gasolina '))
    if (0.01 <= precoGas <= 10):
        break

while True:
    rendAlcool = float(input('rendimento alcool '))
    if (0.01 <= rendAlcool <= 20):
        break
    
while True:
    rendGas = float(input('rendimento gasolina '))
    if (0.01 <= rendGas <= 20):
        break

cAlcool = precoAlcool/rendAlcool #preco por km
cGas = precoGas/rendGas #preco por km

if cAlcool < cGas:
    print('A')
else:
    print('G')
