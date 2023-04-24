"""6) Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de 
saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos
três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os
saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando
não for informado o nome do atleta, apenas a letra ‘O’. """

x = []
menorSalto = 10
maiorSalto = 0
soma = 0
ordinario = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']

nome = input("nome do atleta ")

for i in range(5):
    x.append(float(input(f"{ordinario[i]} salto: ")))
    if x[i] < menorSalto:
        menorSalto = x[i]
    if x[i] > maiorSalto:
        maiorSalto = x[i]

x.remove(menorSalto)
x.remove(maiorSalto)

for i in range(3):
    soma += x[i]
media = soma/3

print(f'atleta: {nome}\n')
print(f'melhor salto: {maiorSalto:.1f}m')
print(f'pior salto: {menorSalto:.1f}m')
print(f"média dos demais saltos: {media:.1f}m\n")
print(f"resultado final: {nome}: {media:.1f}m")
