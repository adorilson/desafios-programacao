def work(inp):
    ESQ = "esquerda"
    DIR = "direita"
    NENHUMA = "nenhuma"
    DUAS = "as duas"

    IN = "ingles"
    FR = "frances"
    PT = "portugues"
    CAIU = "caiu"

    out = {ESQ: IN, DIR: FR, NENHUMA:PT, DUAS:CAIU}
    
    return out[inp]

while True:
    try:
        print(work(input()))
    except EOFError:
        break
