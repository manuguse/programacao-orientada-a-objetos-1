def calcula_horario():  
    chegada = saida + tempo + novo_fuso
    if chegada > 24:
        resto_hora = chegada%24
        chegada = resto_hora
    elif chegada < 0:
        chegada += 24
    print(chegada)

while True:
    saida = int(input('hora de saida '))
    if saida == 24:
        saida = 0
    if 0 <= saida <= 23:
        break
while True:
    tempo = int(input('tempo de viagem '))
    if 1 <= tempo <= 12:
        break
while True:
    novo_fuso = int(input('diferença de fuso '))
    if -5 <= novo_fuso <= 5:
        break
        
calcula_horario() 
