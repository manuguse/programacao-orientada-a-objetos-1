# exercicio 1051

salario = float(input('insira seu salário '))

taxa1 = (salario-2000)*0.08
taxa2 = (salario-3000)*0.18
taxa3 = (salario-4500)*0.28

if (salario <= 2000):
    print('imposto = isento')
elif (salario <= 3000):
    print('imposto = ', taxa1)
elif (salario <= 4500):
    print('imposto = ', taxa2 + 1000*0.08)
else:
    print('imposto = ', taxa3 + 1000*0.08 + 1500*0.18)
