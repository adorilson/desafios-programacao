n1, n2 = input().split(" ")
n1, n2 = min(int(n1), int(n2)), max(int(n1), int(n2))

div = 0
for x in range(1, n1+1):
    if not n1 % x and not n2 % x:
        div = div + 1

print(div)
