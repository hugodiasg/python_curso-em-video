""" ' Crie um programa
onde d jogadores
jtoguum um dado &
enham resultados

aleatórios. Guarde
aesses resultados em
um dicionário. No final,
coloque esse
dicionário em ordem,
sabendo que o
vencaedor tirou o maior
número no dado. """
from random import randint
from operator import itemgetter
ranking={}
jogo={'jogador1': randint(1,6),
      'jogador2': randint(1,6),
      'jogador3': randint(1,6),
      'jogador4': randint(1,6) 
}
print("Valores sorteados: ")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")


print("RANKING: ")
ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
for i, v in enumerate(ranking):
    print(f"O {i+1}o lugar: {v[0]} com {v[1]}")