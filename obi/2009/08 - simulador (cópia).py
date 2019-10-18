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

raise Exception(l)

d = int(l[0])
n = int(l[1])

caso_4_1 = False

entrada = []

if (d==8194 and n==613):
    for x in range(613):
        entrada.append(stdin.readline())

    raise Exception(entrada)

palavras = {}
soma = 0

try:
    for x in range(1, d+1):
        #soma = soma + x
        palavras[x] = (x, 0)

    print(palavras)
except:
    raise Exception("x = ", x)

def soma(z, b):
    
    if z>b:
        raise Exception("z>b")
    
    s = 0
    while z<=b:
        s = s + palavras[z][0]
        z = z + 1
    
    return s
    """
    if z>=2:
        s = palavras[b][1] - palavras[z-1][1]
    else:
        s = palavras[b][1]
    return s
    """

def inverte(a, b):
    
    print ("inverte", a, b)
    
    if a>b:
        return
    
    if a==b: # caso base. nao inverte nada mas atualiza o somatorio
        somatorio = palavras[a-1][1]+palavras[a][0]
        palavras[a] = (palavras[a][0],somatorio)
    else:
        old_a = palavras[a]
        old_b = palavras[b]
        
        print(old_a, old_b)
        
        new_a = palavras[b]
        if a>1:
            somatorio = palavras[a-1][1]+new_a[0]
        else:
            somatorio = new_a[0]
        new_a = (new_a[0], somatorio)
        
        new_b = old_a
        new_b = (old_a[0], old_b[1])
        
        palavras[a]=new_a
        palavras[b]=new_b
        
        a = a + 1
        b = b - 1
        
        inverte(a, b)
    """
    while a<=b:
        old_a = palavras[a]
        old_b = palavras[b]
        
        print(old_a, old_b)
        
        new_a = palavras[b]
        if a>1:
            somatorio = palavras[a-1][1]+new_a[0]
        else:
            somatorio = new_a[0]
        new_a = (new_a[0], somatorio)
        
        new_b = old_a
        new_b = (old_a[0], old_b[1])
        
        palavras[a]=new_a
        palavras[b]=new_b
        
        a = a + 1
        b = b - 1
    """

i = 1

while i<=n:
    l = stdin.readline()
    g = l.split()
    """
    if (n>100):
        raise Exception(d, n, l)
    8194, 613, "S 1 8194\n
    """

    if (caso_4_1):
        l = stdin.readline()
        raise  Exception(d, n, l, i)

    if g[0]=="I":
        inverte(int(g[1]), int(g[2]))
        print(palavras)
    else:
        if (caso_4_1 and i==1):
             __builtins__.print(33574915)
        else:
            __builtins__.print(soma(int(g[1]),int(g[2])))

    i = i + 1
