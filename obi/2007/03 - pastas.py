#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright 2016 Adorilson Bezerra <adorilson@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

DEBUG = False # just debug

def print(*args, **kwargs):
    """My custom print() function."""
    # Adding new arguments to the print function signature 
    # is probably a bad idea.
    # Instead consider testing if custom argument keywords
    # are present in kwargs
    if DEBUG:
        return __builtins__.print(*args, **kwargs)

pn = input().split()

posicoes = int(pn[0]) # abas
total_pastas = int(pn[1]) # total de pastas
slots_completos = total_pastas // posicoes

slots_incompletos = total_pastas % posicoes

# calculando pastas na ultima aba
if (total_pastas % posicoes)==0:
    pastas_na_ultima_aba = posicoes # talves posicoes seja melhor...
else:
    pastas_na_ultima_aba = total_pastas % posicoes

print(posicoes, total_pastas, slots_completos, pastas_na_ultima_aba)

pastas = {}

def general_cases():
    global pn
    global pastas
    global numero_pasta
    global total_pastas
    global posicoes
    global slots_completos
    
    ok = True
    
    items = pastas.items()

    for x in items:
        numero_pasta = x[0]
        quantidade = x[1]
        
        if slots_incompletos==0:
            if quantidade!=total_pastas / posicoes:
                raise Exception(pastas, pn)
                ok = False
                break
            else:
                continue
        
        if numero_pasta<=pastas_na_ultima_aba:
            if quantidade!=slots_completos+1:
                ok = False
                break
        else:
            if quantidade!=slots_completos:
                ok = False
                break

    if ok:
        __builtins__.print("S")
    else:
        __builtins__.print("N")

# lendo as pastas da entrada padrao
import sys
for i in range(total_pastas):
    x = int(sys.stdin.readline()) # isso é mais rápido que input()
    try:
        pastas[x] = pastas[x] + 1
    except KeyError:
        pastas[x] = 1
    
general_cases()
