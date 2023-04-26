def verificaAdicao():
    while True:
        x = input('deseja adicionar alguem? ').upper()
        if x == 'S' or x == 'N':
            break
    return x

def verificaModalidade():
    while True:
        x = int(input('escolha a modalidade (1/2) '))
        if x == 1 or x == 2:
            break
    return x

def insereCliente():
    x = input('insira o nome do cliente ')
    return x

empresa1 = {'alice','bruno','carla','douglas'}
empresa2 = {'elaine','fabio','gabriel','alice','douglas'}

print(f'clientes empresa 1: {empresa1}')
print(f'clientes empresa 2: {empresa2}')

while True:
    adicionar = verificaAdicao()
    if adicionar == 'N':
        break
    else:
        modalidade = verificaModalidade()
        if modalidade == 1:
            empresa1.add(insereCliente())
        elif modalidade == 2:
            empresa2.add(insereCliente())
    
if empresa1.isdisjoint(empresa2) == False:
    print(f'\nclientes repetidos: {empresa1.intersection(empresa2)}')
    
print(f'qtde clientes empresa 1: {len(empresa1)}')
print(f'qtde clientes empresa 2: {len(empresa2)}')
print(f'qtde clientes ambas empresas: {len(empresa1.intersection(empresa2))}')
print(f'qtde clientes apenas uma empresa: {len(empresa1.symmetric_difference(empresa2))}')
print(f'total clientes: {len(empresa1.union(empresa2))}')
