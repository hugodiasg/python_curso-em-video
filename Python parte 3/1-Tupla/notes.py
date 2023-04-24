# Tuplas
print('------------------------------------------------------------Tuplas')
#   Tuplas são IMUTÁVEIS (só podem ser alteradas na sua declaração)
lanche=('Hamburguer','Pizza','Suco','Pudim')
print(lanche)
print(f"lanche 2 é {lanche[2]}")
print(f"lanche 0 ao 2 é {lanche[0:3]}") ## Sempre é ignorado o último índice da Tupla
print(f"lanche -1 é {lanche[-1]}")

for comida in lanche:
    print(f'Vou comer {comida}')

for posicao,comida in enumerate(lanche):
    print(f"Comida {comida} na posição {posicao}")

tupla2=('bla','ble','blu')
tupla_resultado=lanche+tupla2
print(f"Somando tuplas {lanche} e {tupla2} = {tupla_resultado}")
print(f'Pizza está em comida {lanche.count("Pudim")} vezes')
del(comida)