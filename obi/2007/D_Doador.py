e = input().split(' ')

dinheiro_inicial = float(e[0])
doacao = float(e[1])
juros = float(e[2])
minimo = float(e[3])

meses = 0

dinheiro = dinheiro_inicial

while minimo<dinheiro:
    dinheiro_juros = dinheiro * (juros/100)
    dinheiro_doacao = dinheiro * (doacao/100)
    dinheiro = dinheiro + dinheiro_juros - dinheiro_doacao
    

print(meses)
