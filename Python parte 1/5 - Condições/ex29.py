'''
e Escreva um
programa que fafa o
computodor “pensar”
em um número intairo
entre 0 e 5 ca pera para
o usuário tentar
descobrir qual foi o
número escolhido pelo
computador.

O programa deverá
escrever na taelaseo
usuário venceu ou
perdeu.

'''
import random

n=random.randint(0,5)
n_user=input("Chute um número de 0 a 5: ")
if int(n_user)==n:
    print("Você acertou!")
else:
    print(f"Você errou,o número certo é {n}")


