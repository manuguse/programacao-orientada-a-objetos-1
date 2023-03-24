while True:
    N = int(input())
    if (0 <= N <= 13):
        break
f = 1
const = N

while (const > 0):
    f *= const
    const -= 1
    
print(f)
