# exerício 2409

A = int(input('profundidade colchão '))
B = int(input('largura colchão '))
C = int(input('altura colchão '))
H = int(input('altura porta '))
L = int(input('largura porta '))

#	  LARGURA		    ALTURA
if (B <= L) and (A <= H):
    print('S')
if (B <= L) and (C <= H):
    print('S')
elif (C <= L) and (B <= H):
    print('S')
elif (C <= L) and (A <= H):
    print('S')
elif (A <= L) and (C <= H):
    print('S')
elif (A <= L) and (B <= H):
    print('S')
else:
    print('N')
