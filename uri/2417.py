# exercício 2417

    vitoriaC = int(input('vitórias cormengo '))
    empateC = int(input('empates cormengo ')) 
    saldoC = int(input('saldo cormengo '))

    vitoriaF = int(input('vitórias flaminthians '))
    empateF = int(input('empates flaminthians ')) 
    saldoF = int(input('saldo flaminthians '))

    pontosC = vitoriaC*3 + empateC
    pontosF = vitoriaF*3 + empateF

    if (pontosC > pontosF):
        print('C')
    elif (pontosF > pontosC):
        print('F')
    elif (saldoC > saldoF):
        print('C')
    elif (saldoF > saldoC):
        print('F')
    else:
        print('=')
