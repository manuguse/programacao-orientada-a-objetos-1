def soma(inicio, fim):
    soma = 0
    for i in range(inicio, fim+1):
        soma += i
    print(soma)
    
def subtracao(a, b):
    if a > b:
        sub = a - b
    else:
        sub = b - a
    print(sub)

while True: 
    inicio = int(input('inicio: '))
    fim = int(input('fim: '))

    soma(inicio, fim)
    
    a = int(input('a: '))
    b = int(input('b: '))
    
    subtracao(a, b)
    
    while True:
        parada = str(input('deseja continuar? ')).upper()
        if parada == 'S' or 'N':
            break
    if parada == 'N':
        break
