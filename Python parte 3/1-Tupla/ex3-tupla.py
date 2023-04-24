"""
' Crieumprograma
quevaigerarcinco |
números aleatórios e
colocar em uma tupla. —
Dapois disso. mostraa
Iistuãnln denúmeros —
garados a também |
Indique o menorego ;
maior valor queastão :-
na tupla. |
"""
from random import randint
n=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Valores sorteados {n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')