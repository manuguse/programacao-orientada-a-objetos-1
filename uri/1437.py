while True:
    num = int(input('numero de comandos '))
    if num == 0:
        break
    
    while True:
        comando = input('insira os comandos ').upper()
        if len(comando) == num:
            break
        print('a quantidade de comandos deve ser igual à previamente informada ')

    direcao = 1

    for i in range (num):
        if comando[i] == 'D':
            direcao += 1
        elif comando[i] == 'E':
            direcao -= 1
    
    direcao = direcao%4
    
    if direcao == 1:
        direcao = 'N'
    if direcao == 2:
        direcao = 'L'
    if direcao == 3:
        direcao = 'S'
    if direcao == 4:
        direcao = 'O'
