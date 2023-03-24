par = 0
impar = 0
pos = 0
neg = 0

for i in range (5):
    num = int(input('numero '))
    if (num%2 == 0):
        par += 1
    else:
        impar += 1
    if (num > 0):
        pos += 1
    elif (num < 0):
        neg += 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')    
print(f'{pos} valor(es) positivo(s)')    
print(f'{neg} valor(es) negativo(s)')
