# exercício 2568

D = int(input('dia inicial '))
I = float(input('valor inicial ')) 
X = float(input('mundança de valor '))
F = int(input('dias futuros '))

if (D%2 == 0) and (F%2 == 0):
   valorFinal = I
elif (D%2 == 0) and (F%2 == 1):
    valorFinal = (I - X)
elif (F%2 == 0):
    valorFinal = I
elif (F%2 == 1):
    valorFinal = (I + X)
    
print(valorFinal)
