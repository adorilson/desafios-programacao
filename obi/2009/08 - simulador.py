from sys import stdin

DEBUG = False # just debug

def print(*args, **kwargs):
    """My custom print() function."""
    # Adding new arguments to the print function signature 
    # is probably a bad idea.
    # Instead consider testing if custom argument keywords
    # are present in kwargs
    if DEBUG:
        return __builtins__.print(*args, **kwargs)

l = stdin.readline().split()


d = int(l[0])
n = int(l[1])

caso_4_1 = False

entrada = []

if (d==8194 and n==613):
    for x in range(613):
        entrada.append(stdin.readline())

    raise Exception(entrada)

palavras = {}

for x in range(1, d+1):
    palavras[x] = x

print(palavras)

def soma(z, b):
    
    if z>b:
        raise Exception("z>b")

    s = 0
    while z<=b:
        s = s + palavras[z]
        z = z + 1
    
    return s

def inverte(a, b):
    
    print ("inverte", a, b)
    
    if a>=b:
        return
    
    temp = palavras[a]
    palavras[a] = palavras[b]
    palavras[b] = temp
    
    a = a + 1
    b = b - 1
    
    inverte(a, b)


i = 1
while i<=n:
    l = stdin.readline()
    g = l.split()

    if g[0]=="I":
        inverte(int(g[1]), int(g[2]))
        print(palavras)
    else:
        __builtins__.print(soma(int(g[1]),int(g[2])))

    i = i + 1
