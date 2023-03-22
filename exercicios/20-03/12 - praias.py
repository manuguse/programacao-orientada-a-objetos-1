n = int(input('insira o número de praias de deseja cadastrar '))
somaDistancia = 0
qtdeEntre = 0

for i in range (n):
    nome = str(input('nome praia '))
    distancia = int(input('distancia do centro '))  
    somaDistancia += distancia
    
    if (15 < distancia < 20):
        qtdeEntre += 1
        
    if (i == 0):
        maiorDistancia = distancia
        maiorNome = nome
    elif (distancia > maiorDistancia):
        maiorDistancia = distancia
        maiorNome = nome

print(f'a mais distante é {maiorNome}, com {maiorDistancia}km de distância')
print(f'há {qtdeEntre} praia(s) entre 15 e 20km do centro')
print(f'a média das distâncias é de {somaDistancia/n}km')
