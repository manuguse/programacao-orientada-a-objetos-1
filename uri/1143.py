while True:
    N = int(input('numero '))
    if (1 < N < 1000):
        break

for i in range (1, N+1):
    a = i
    b = i**2
    c = i**3
    print(f'{a} {b} {c}')
