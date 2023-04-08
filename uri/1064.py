somaPos = 0
pos = 0

for i in range (6):
    num = float(input('numero: '))
    if num > 0:
        pos += 1
        somaPos += num

print(f'{pos} valor(es) positivo(s)')
print(f'{somaPos/pos:.2f}')
