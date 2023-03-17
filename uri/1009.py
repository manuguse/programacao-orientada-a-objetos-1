# exemplo 1009 

nome = input('insira o nome ')
salario = float(input('insira o salário '))
valorVendido = float(input('insira o valor vendido '))
salarioTotal = float(salario + valorVendido*0.15)

print('TOTAL = R${:.2f}'.format(salarioTotal))
