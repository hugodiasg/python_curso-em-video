"""
o Cria um programa
que tenha uma tupla
com várias palavras
(nao usar acentos).
Dapois disso. você
deva mostrar. para
cada palavra, quais
SAO a5 suas vogais.
"""

tupla=("Abacate","Cadeira","Computador","Loja","Arara","Paralelepipedo")
vogais=""
for t in tupla:
    if t.count('a')>0:
        vogais+=" a"
    if t.count('e')>0:
        vogais+=" e"
    if t.count('i')>0:
        vogais+=" i"
    if t.count('o')>0:
        vogais+=" o"
    if t.count('u')>0:
        vogais+=" u"
    print(f"Em {t} tem as vogais: {vogais}")
    vogais=""