""" ' Fa£Fa um programa
ET quudu umnjogudur
EE ic
palpitas. O programa
vai parguntar quantos
EcA surãaêurudos [
vai sortear 6 números
ESA cccc
jtugu. cadastrando
udo em uma lista

[ aaA """


jogos=[]
from random import randint
num_palpites=int(input("Número de jogos: "))

i=1
j=1
for i in range(num_palpites):
    palpites=[]
    while len(palpites)<6:
        num_aleatorio=randint(1,60)
        if not num_aleatorio in palpites:
            palpites.append(num_aleatorio)
    print(f"Palpite {i+1}: {palpites}")
