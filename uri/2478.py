todos = {}

x = int(input())
for i in range(x):
    entrada = input().lower().split()
    pedido = [entrada[1], entrada[2], entrada[3]]
    todos[entrada[0]] = pedido

while True:
    chute = input().lower().split()
    if chute == 'eof':
        break
    if chute[1] in todos[chute[0]]:
        print(f'uhul, seu amigo secreto vai adorar o/')
    else:
        print('tente novamente')
