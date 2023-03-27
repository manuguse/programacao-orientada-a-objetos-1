from math import ceil
numeroVolta = 0

while True: # mais rapido
    x = int(input('x '))
    if (1 <= x <= 10000):
        break
    
while True: # mais lento
    y = int(input('y '))
    if (1 <= y <= 10000):
        break

while True:
    numeroVolta += 1
    var = ceil((x/y)*numeroVolta)
    if numeroVolta > var:
        print(numeroVolta)
        break
