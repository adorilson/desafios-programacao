input()
V = [int(i) for i in input().split()]

d = {}

for i, a in enumerate(V):
    indexes = d.get(a, [])
    indexes.append(i)
    d[a] = indexes

#print('d', d)

for i, ai in enumerate(V):
    achei = False
    for aj in range(ai+1, 101):
        try:
            j = V.index(aj, i+1)
        except ValueError:
            pass
        else:
            print(aj, end=' ')
            achei = True
            break          
    if not achei:
        print('*', end=' ')
    
#print(d)
