exp = input()

exp = exp.replace('7', '0').replace('x','*')
a, op, b = exp.split(' ')

if op=='+':
    result = int(a) + int(b)
else:
    result = int(a) * int(b)

print(int(str(result).replace('7', '0')))
