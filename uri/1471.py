def verifica():
    while True:
        x = (input().split(" "))
        if 1 <= int(x[0]) <= 10*4 and 1 <= int(x[1]) <= 10*4:
            break
    return x

while True:
    n, r = verifica()
    voltaram = input().split(" ")
    naoVoltaram = []
    if n == r:
        print("*")
    else:
        for i in range (1, int(n)+1):
            if str(i) not in voltaram:
                naoVoltaram.append(i)
        print(sorted(naoVoltaram))
