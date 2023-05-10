def verifica(a,b):
    while True:
        x = int(input())
        if a <= x <= b:
            break
    return x

alturaPulo = verifica(1,5)
numeroCanos = verifica(2,100)
alturaCanos = input().split(" ")

perdeu = 0

for i in range(numeroCanos - 1):
    if int((alturaCanos[i+1])) - int((alturaCanos[i])) > alturaPulo:
        print("GAME OVER")
        perdeu += 1
        break

if perdeu == 0:
    print("YOU WIN")
