# exemplo 1019

inserirSegundos = int(input('segundos '))
hora = int(inserirSegundos/3600)
restoHora = int(inserirSegundos%3600)
minuto = int(restoHora/60)
restoMinuto = int(restoHora%60)
segundo = restoMinuto

print(f'{hora}:{minuto}:{segundo}')
