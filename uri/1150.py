def ultrapassa(x, z):
    soma = 0
    cont = 0
    while soma <= z:
        cont += 1
        soma += x
        x += 1
    print(cont)
    
x = int(input('x '))
while True:
    z = int(input('z '))
    if z > x:
        break
ultrapassa(x, z)
