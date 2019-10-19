"""
Questão adaptada de: https://olimpiada.ic.unicamp.br/pratique/i1/2016/f1/basquete/
"""

def basquete(time):
    
    if 'S' not in time or 'U' not in time:
        if 'L' in time:
            return 'invalida'
    if 'P' in time and 'L' in time:
        return 'invalida'
    if 'C' in time and 'P' in time:
        return 'invalida'
                                    
    alas = 0                
    armadoras = 0           
    pivos = 0               
    if 'Q' in time:
        alas = alas + 1
    if 'S' in time:
        alas = alas + 1
    if 'U' in time:
        alas = alas + 1
                            
    if 'A' in time:
        armadoras = armadoras + 1
    if 'C' in time:
        armadoras = armadoras + 1
    if 'E' in time:
        armadoras = armadoras + 1
                            
    if 'L' in time:
        pivos = pivos + 1
    if 'N' in time:
        pivos = pivos + 1
    if 'P' in time:
        pivos = pivos + 1
                         
    if alas == 0:
         return 'invalida'
    if pivos == 0:
        return 'invalida'
    if armadoras == 0:
        return 'invalida' 
                         
    if armadoras > 1 and alas > 1:
        return 'invalida'
                               
    return 'valida'
    
print(basquete('ACLNS'))
print(basquete('C L P S U'))
print(basquete('A E N P U'))
print(basquete('A E L S U'))
print(basquete('L N Q S U'))






