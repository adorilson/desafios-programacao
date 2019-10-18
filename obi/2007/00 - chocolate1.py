"""
n = int(input())
i = 1
qtd = 0
while i<=n:
    p = int(input())
    qtd = qtd + p - 1
    i = i + 1

print(qtd)
"""

n = input()
divisoes = input()
divisoes = divisoes.split()

qtd = 0

for p in divisoes:
    p = int(p)
    qtd = qtd + p - 1

print(qtd)
