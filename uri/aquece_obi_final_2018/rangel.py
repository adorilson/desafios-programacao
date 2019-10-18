input()
V = [int(i) for i in input().split()]

uniq_V = V[:]
uniq_V.reverse()

#print('uniq_V', uniq_V)

maximum = max(V)

#print('V', V)

for i, ai in enumerate(V):
    if i==len(V)-1: # ultimo elemento
        __builtins__.print('*')
    else:
        if ai==maximum:
            __builtins__.print('*', end=' ')
            continue
         
        ai_pos = uniq_V.index(ai)
        try:
            next = uniq_V[ai_pos-1]
            
            next_pos_V = V.index(next)
            #print('ai, next, next_pos_V', ai, next, next_pos_V)
        except:
            output = '*'
        else:
            #print('next_pos_V, i', next_pos_V, i)
            if next_pos_V>i:
                output = next
            else:
                output = '*'
                #print('else')
        __builtins__.print(output, end=' ')
    
    """
    achei = False
    if ai < maximum:
        for j, aj in enumerate(V[i+1:]):
            if aj>ai:
                __builtins__.print(aj, end=' ')
                achei = True
                break
        if (not achei):
            if (i == len(V)-1):
                __builtins__.print('*')
            else:
                __builtins__.print('*', end=' ')    
    else:
        __builtins__.print('*', end=' ')
    """            
#for x in R[:-1]:
#    __builtins__.print(x, end=" ")

#__builtins__.print(R[len(R)-1], end='')
