"""
' Crie uma tupla |
preenchidacomos 20—
primeiros colocados —
da Tabela do |
Campeonato Brasileiro -
deFutebol.naordem —
decolocafao.Depois —
mostre: |
A) Apenasos5 |
primeiros colocados. —
BIOs últimos 4 |
colocados da tabela. —
C) Uma lista comos ]
timas em ordem |
alfabética. |
D) Em que posifao na |
tabelaastáotimeda |
Cruzeiro. |
"""
colocados_brasileirao=('América-MG','Athetico-PR','Bahia','Botafogo','Bragantino','Corinthians','Coritiba','Cruzeiro','Cuiabá','Flamengo','Fluminense','Fortaleza','Goiás','Grêmio','Internacional','Palmeiras','Santos','São Paulo','Vasco')
tamanho_tupla=len(colocados_brasileirao)

print(f'a) Os 5 primeiros colocados são: {colocados_brasileirao[0:5]}')
print(f'Os 4 últimos colocados são: {colocados_brasileirao[(tamanho_tupla-4):tamanho_tupla]}')
print(f'A tupla em ordem alfabética é: {sorted(colocados_brasileirao)}')
print(f'Cruzeiro está na posição {colocados_brasileirao.index("Cruzeiro",0,tamanho_tupla)+1}ª')