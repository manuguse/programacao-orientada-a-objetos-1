# exemplo 1017

tempo = int(input('horas levadas '))
velMedia = int(input('velocidade média '))
distancia = int(velMedia*tempo)
capacidade = 12 #km/l
litros = distancia/capacidade

print('{:.3f}'.format(litros))
