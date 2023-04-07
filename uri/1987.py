while True:
    alg, num = input(' ').split(' ')
    if 1 <= int(alg) <= 10 and 1 <= int(num) <= 1000000000:
        break
    print('valor(es) invalido(s)')
    
somaNum = 0

for i in range(int(alg)):
    somaNum += int(num[i])
    
if somaNum%3 == 0:
    resposta = 'sim'
else:
    resposta = 'nao'

print(somaNum, resposta)
