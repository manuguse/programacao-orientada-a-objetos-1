def sensor_capacidade(leituras, maxima_cap):
    total = 0
    excedido = 0
    for i in range (leituras):
        saida = int(input('saidas '))
        entrada = int(input('entradas '))
        total += entrada - saida
        if total > maxima_cap:
            excedido += 1
    if excedido >= 1:
        print('S')
    else:
        print('N')

leituras = int(input('numero de leituras '))
maxima_cap = int(input('capacidade maxima '))
sensor_capacidade(leituras, maxima_cap)
