while True: 
    somaDif = 0

    while True:
        num = int(input('numero: '))
        if (0 <= num <= 100):
            break

    for i in range (num):
        
        while True: # joao
            j = int(input('J: '))
            if (0 <= j <= 100):
                break

        while True: # zezinho
            z = int(input('Z: '))
            if (0 <= z <= 100):
                break

        dif = j - z
        somaDif += dif
        print(somaDif)

    if num == 0:
        break
