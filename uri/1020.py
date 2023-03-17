# exemplo 1020

inserirDias = int(input('insira a idade em dias '))
anos = int(inserirDias/365)
restoAnos = int(inserirDias%365)
mes = int(restoAnos/30)
restoMes = int(restoAnos%30)
dia = restoMes
    
print(anos, 'ano(s)')
print(mes, 'mes(es)')
print(dia, 'dia(s)')
