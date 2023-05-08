while True:
    q = int(input())
    if 3 <= q <= 233000:
        break

while True:
    cont = 0
    v = input().split(" ")
    if len(v) != q:
        continue
    for i in range(q):
        if 0 <= int(v[i]) <= 1:
            cont += 1
    if cont == q:
        break

insat = 0
sat = 0

for i in range(q):
    if v[i] == "1":
        insat += 1
    else:
        sat += 1

if sat > (q/2):
    print("y")
else:
    print("n")
