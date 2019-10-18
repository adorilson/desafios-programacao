import sys

N, M, K = sys.stdin.readline().split(' ')

N = int(N)
M = int(M)
K = int(K)

linha = [0]*M
grid = [linha]*N

for x in range(1, int(K)+1):
    player = ['P', 'R', 'H', 'C'][x%4]
    
    D, X = sys.stdin.readline().split()
    X = int(X)
    if D=='L':
        grid[X-1] = [player]*M
    else:
        for i in grid:
            i[X-1] = player

pounts = {'R':0, 'H':0, 'C':0, 'P':0} 
for x in grid:
    for i in x:
        if i:
            pounts[i] = pounts[i] + 1
        
print('R' + str(pounts['R']), 'H' + str(pounts['H']), 'C' + str(pounts['C']), 'P' + str(pounts['P']))

