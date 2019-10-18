
"""
x = input()
presentes = {}
for i in range(int(x)):
    aluno = input()
    if not aluno in presentes:
        presentes[aluno] = True

print(len(presentes))
"""

x = input()
presentes =[]
for i in range(int(x)):
    aluno = input()
    presentes.append(aluno)
    
s = set(presentes)
print(len(s))
