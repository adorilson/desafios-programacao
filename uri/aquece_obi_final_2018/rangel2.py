# wrong answer

input()
V = [int(i) for i in input().split()]

d = {}

for i, a in enumerate(V):
    indexes = d.get(a, [])
    indexes.append(i)
    d[a] = indexes

#print('d', d)

for i, ai in enumerate(V):
    temp_index = 100000
    temp_aj = -1
    for aj in range(i+1, 101):
        indexes = d.get(aj, 0)
        if indexes:
            for j in indexes:
                if j>i and j<temp_index:
                    temp_aj = aj
                    temp_index = j
    
    end = ' '
    if i==len(V)-1:
        end='\n'
        
    if temp_aj==-1:
        temp_aj='*'
    
    print(temp_aj, end=end)             
    
#print(d)
