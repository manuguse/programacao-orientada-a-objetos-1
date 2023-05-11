import random

print("-------------------------")
print("    JOGA NA MEGA SENA")
print("-------------------------")
num = int(input("quantos jogos voce quer que eu sorteie? "))
while num < 0:
    num = int(input("o numero deve ser maior que 0 "))
print("-=- SORTEANDO 4 JOGOS =-=")
jogos = []
for i in range(num):
    jogoI = []
    for j in range(6):
        jogoI.append(random.randint(1,61))
    jogos.append(jogoI)
    print(f"jogo {i+1}: {jogos[i]}")
print("-=-= < BOA SORTE! > -=-=")
