def confere_primo(num):
    for i in range(2, num):
        if num%i == 0:
            return 'composto'
    return 'primo'

somaComposto = 0
somaPrimo = 0

num = int(input('num '))
for i in range (1, num + 1):
    tipo = confere_primo(i)
    if tipo == 'composto':
        somaComposto += 1
    else:
        somaPrimo += 1
        
print(somaPrimo, somaComposto)
