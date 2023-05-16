def verificaNum():
    while True:
        x = int(input())
        if 1 <= x <= 100:
            break
    return x

n = verificaNum()
traducoes = {}
for i in range(n):
    lingua = input()
    traducoes[lingua] = input()
m = verificaNum()
for i in range(m):
    nome = input()
    lingua = input()
    print(nome)
    print(traducoes[lingua])
    print()
