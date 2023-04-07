def calcula_salario():
    if atual_sal > 2000:
        novo_sal = atual_sal*1.04
        percentual = '4'
    elif atual_sal > 1200:
        novo_sal = atual_sal*1.07
        percentual = '7'
    elif atual_sal > 800:
        novo_sal = atual_sal*1.10
        percentual = '10'
    elif atual_sal > 400:
        novo_sal = atual_sal*1.12
        percentual = '12'
    else:
        novo_sal = atual_sal*1.15
        percentual = '15'
    
    reajuste = novo_sal - atual_sal

    print(f'novo salário: {novo_sal:.2f}')
    print(f'reajuste ganho: {reajuste:.2f}')
    print(f'em percentual: {percentual} %')
    
atual_sal = float(input('salario atual '))
calcula_salario()
