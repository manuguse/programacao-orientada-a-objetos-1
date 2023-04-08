somaIdade = 0
cont = 0

while True:
    num = int(input('idade: '))
    if num < 0:
        break
    somaIdade += num
    cont += 1
    media = somaIdade/cont

print(f'a média das idades é {media:.2f}')
