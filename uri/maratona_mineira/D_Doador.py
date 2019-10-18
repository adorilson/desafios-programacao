e = input().split(' ')

dinheiro_inicial = float(e[0])
doacao = float(e[1])
juros = float(e[2])
minimo = float(e[3])

meses = 0

dinheiro = 10**18

while True:
    dinheiro_juros = dinheiro * (juros/100)
    if dinheiro_juros<=minimo:
        break
    dinheiro_doacao = dinheiro * (doacao/100)
    dinheiro = dinheiro - dinheiro_doacao
    #print(dinheiro, dinheiro_juros)
    meses = meses + 1

if meses>1:
    meses = meses - 1
print(meses)
