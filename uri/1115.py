def quadrante():
    if x == 0 or y == 0:
        quadrante = 'nenhum'
    if x > 0:
        if y > 0:
            quadrante = 'primeiro'
        elif y < 0:
            quadrante = 'quarto'
    elif x < 0:
        if y > 0:
            quadrante = 'segundo'
        elif y < 0:
            quadrante = 'terceiro'
    print(quadrante)

x, y = (input('x, y: ')).split(' ')
x = int(x)
y = int(y)
quadrante()
