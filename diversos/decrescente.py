"""
Implementacao de ordenação decrescente de
três valores utilizando repetição
"""

X = int(input("X:"))
Y = int(input("Y:"))
Z = int(input("Z:"))

while (X<Y or Y<Z):
    if X < Y:
        X, Y = Y, X
    
    if Y < Z:
        Y, Z = Z, Y

print(X, Y, Z)
