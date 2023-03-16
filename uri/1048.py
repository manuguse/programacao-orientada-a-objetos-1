# exercício 1048

salario = float(input('insira seu salário '))

if (salario <= 400):
    novoSalario = salario*1.15
    percentual = '15 %'
elif (salario <= 800):
    novoSalario = salario*1.12
    percentual = '12 %'
elif (salario <= 1200):
    novoSalario = salario*1.10
    percentual = '10 %'
elif (salario <= 2000):
    novoSalario = salario*1.07
    percentual = '7 %'
else:
    novoSalario = salario*1.04
    percentual = '4 %'
    
reajuste = novoSalario - salario
print('Novo salário: R${:.2f}'.format(novoSalario))
print('Reajuste ganho: R${:.2f}'.format(reajuste))
print('Em percentual:', percentual)
