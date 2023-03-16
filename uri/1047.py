# exercício 1047

hora1 = int(input('hora inicial '))
min1 = int(input('minuto inicial '))
hora2 = int(input('hora final '))
min2 = int(input('minuto final '))

tempo1_min = hora1*60 + min1
tempo2_min = hora2*60 + min2

if (hora2 > hora1):
    duracaoMin = tempo2_min - tempo1_min
    horas = int(duracaoMin/60)
    minutos = int(duracaoMin%60)
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

elif (hora1 > hora2):
    duracaoMin = 24*60 - tempo1_min + tempo2_min
    horas = int(duracaoMin/60)
    minutos = int(duracaoMin%60)
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
