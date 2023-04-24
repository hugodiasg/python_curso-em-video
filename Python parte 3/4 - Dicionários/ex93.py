""" Crie um programa
que garencia o
aproveitamento de um
jogador de Ffutebol. O
programa vai ler o
nomea do jogador &
quantaz partidas ele
jogou. Depois voailer q
quantidade de gols
fFaitos em cada
partida. No Final. tudo
is50 será quardado em
um dicionario,.
incluindo o total de
gols feitos durante o
campeonato. """

futebol={'nome':input('Nome do jogador: '),'qtd_partidas':int(input("Quantas partidas jogadas: "))}
gols=[]
aproveitamento=0
for i in range(futebol['qtd_partidas']):
    gols.append(int(input(f"Quantos gols na partida {i+1}? ")))
futebol['gols']=gols[:]
print(futebol)
print("=-"*10)
for i in gols:
    aproveitamento+=i
print(f"Aproveitamento: {aproveitamento} gols")