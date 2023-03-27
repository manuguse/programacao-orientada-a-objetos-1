while True:
    print('Teste')
    valor = int(input('valor '))
    if valor == 0:
        break
    
    i = int(valor/50)
    restoI = valor%50
    
    j = int(restoI/10)
    restoJ = restoI%10
    
    k = int(restoJ/5)
    restoK = restoJ%5
    
    l = int(restoK/1)
    
    print(i,j,k,l)
    print()
