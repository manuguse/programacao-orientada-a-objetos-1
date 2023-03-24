cont = 0
resposta = int(input('insira a resposta '))

for i in range (5):
    while True:
        palp = int(input('insira seu palpite '))
        if (palp > 4) or (palp < 1):
            print('palpite inválido')
        else: 
            break
    if (palp == resposta):
        cont += 1
print(cont)
