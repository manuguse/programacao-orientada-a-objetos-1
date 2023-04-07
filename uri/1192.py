num = int(input('numero de testes '))
for i in range (num):
    sequencia = input('insira a sequencia ')
    if sequencia[0] == sequencia[2]:
        resultado = int(sequencia[0]) * int(sequencia[2])
    elif sequencia[1].isupper() == True:
        resultado = int(sequencia[2]) - int(sequencia[0])
    else:
        resultado = int(sequencia[0]) + int(sequencia[2])
    print(resultado)
