# exercício 1) empréstimo casa

valorTotal = int(input('insira o valor da casa '))
salario = int(input('insira o seu salário '))
anosParaPagar = int(input('insira em quantos anos pretende pagar '))

valorMensal = (valorTotal / (anosParaPagar*12))
if (valorMensal <= (0.3*salario)):
    print(f'a prestação é de R${valorMensal}')
else:
    print('empréstimo negado')

# exercício 2) valor final produto

valorInicial = float(input('valor inicial '))
condicaoDePagamento = int(input('condição desejada '))

if (condicaoDePagamento == 1):
    print(f'o valor final é R${0.9*valorInicial}')
elif (condicaoDePagamento == 2):
    print(f'o valor final é R${0.95*valorInicial}')
elif (condicaoDePagamento == 3):
    print(f'o valor final é R${valorInicial}')
elif (condicaoDePagamento == 4):
    print(f'o valor final é R${1.2*valorInicial}')
else:
    print('condição inválida')

# exercício 3) cálculo de imc

peso = float(input('insira seu peso em kg '))
altura = float(input('insira sua altura em metros '))
imc = peso/(altura**2)

print('seu imc é: {:.1f}'.format(imc))

if (imc > 40):
    print('status: obesidade mórbida')
elif (imc > 30):
    print('status: obesidade')
elif (imc > 25):
    print('status: sobrepeso')
elif (imc > 18.5):
    print('status: peso ideal')
else:
    print('status: abaixo do peso')

# exercício 4) média aluno

a = float(input('primeira nota '))
b = float(input('segunda nota '))
c = float(input('terceira nota '))
media = float((a + b + c)/3)

if (media < 5):
    print('reprovado')
elif (media < 7):
    print('em recuperação')
else:
    print('aprovado')

