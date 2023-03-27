d = int(input('distancia inicial ')) # entre ladra e guarda
vf = int(input('velocidade ladrao '))
vg = int(input('velocidade guarda '))

x = float(d**2 + 144)**(1/2)
tf = 12/vf # tempo fugitivo
tg = x/vg # tempo guarda 

if (tf < tg):
    print('nao')
else:
    print('sim')
