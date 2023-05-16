def ordena():
    for i in range(n):
        for j in range(n):
            if int(v[i]) > int(v[j]):
                v[i], v[j] = v[j], v[i]
    return v
