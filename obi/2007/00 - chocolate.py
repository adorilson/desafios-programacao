input()
lista = input().split()

pedacos = 0
for x in lista:
    pedacos = pedacos + int(x) - 1

print(pedacos)
