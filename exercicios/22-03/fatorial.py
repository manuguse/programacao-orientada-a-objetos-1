n1 = int(input('numero para calcular fatorial '))
const = n1
f = 1

print(f'{n1}! = ', end='')
while const > 0:
    print('{}'.format(const), end='')
    print(' X ' if const > 1 else ' = ', end='')
    f*=const
    const-=1
print(f)
