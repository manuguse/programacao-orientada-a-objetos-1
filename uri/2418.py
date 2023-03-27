contador = 0

for i in range(5):
    nota = float(input('nota: '))
    contador += nota
    if i == 0:
        maiorNota = nota
        menorNota = nota
    else:
        if nota > maiorNota:
            maiorNota = nota
        elif nota < menorNota:
            menorNota = nota

contador = contador - maiorNota - menorNota
print(f'{contador:.1f}')
