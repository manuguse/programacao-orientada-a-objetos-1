# exercício 1036

a = float(input('insira a '))
b = float(input('insira b '))
c = float(input('insira c '))

delta = (b**2 - 4*a*c)

if (delta < 0) or (2*a == 0) :
  print('impossível calcular')
 else:
   raiz1 = (-b + (delta)**1/2)/(2*a)
   raiz2 = (-b - (delta)**1/2)/(2*a)
   print(f'R1 = {raiz1}')
   print(f'R2 = {raiz2}')
