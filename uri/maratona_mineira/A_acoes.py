l = input().split()

D = int(l[0])
I = int(l[1])
X = int(l[2])
F = int(l[3])

price = I

for x in range(D+1, D+F+1):
    if not x % 2:
        price = price + X
    else:
        price = price - X
    
print(price)
