while True:
    N = int(input('nota '))
    if (0 <= N <= 100):
        break

if N == 0:
    conceito = 'E'
elif N < 36:
    conceito = 'D'
elif N < 61:
    conceito = 'C'
elif N < 86:
    conceito = 'B'
else:
    conceito = 'A'

print(conceito)
