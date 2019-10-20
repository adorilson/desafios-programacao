"""
Adaptado de: https://olimpiada.ic.unicamp.br/static/extras/obi2009/provas/ProvaOBI2009_f2i1.pdf
"""

def estacionamento(carros):


    if carros.index('C') not in [0, 5]:
        return 'invalida'

    posicaoV = carros.index('V')
    posicaoD = carros.index('D')
    if abs(posicaoV - posicaoD)!=4:
        return 'invalida'

    posicaoO = carros.index('O')
    posicaoF = carros.index('F')
    if abs(posicaoO - posicaoF)<2:
        return 'invalida'

    return 'valida'

print(estacionamento('VCDHFO'))
print(estacionamento('VHOFCD'))
print(estacionamento('VOCFDH'))

print(estacionamento('CDHVFO'))
print(estacionamento('CFDVOH'))
print(estacionamento('CDHOFV'))
print(estacionamento('CFVOHD'))
print(estacionamento('CVOFHD'))

print(estacionamento('FHDVOC'))
print(estacionamento('OHCDFV'))

print(estacionamento('FOCDHV'))
print(estacionamento('DVCHFD'))
print(estacionamento('HDVOFC'))

print(estacionamento('DOHFVC'))
