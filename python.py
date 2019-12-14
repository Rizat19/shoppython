with open('a.txt', 'r')as f:
    a = f.read()
    z = a.split('\n')
    b = []
    re = {}
    for i in z:
        q = i.split(' -')
        b.append(q)

    for i in range(len(b)):
        re[b[i][0]] = b[i][1]
    print(re)
soz = input('Soz engiz :')
print(re[soz])