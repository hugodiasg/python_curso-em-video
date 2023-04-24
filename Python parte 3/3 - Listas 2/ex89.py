""" ' Cria um programa
ETc ENcAO
notas de vários alunos
EA A CE SE RL
ESAc EA dcA
final. nmostre um
EAn a ucA
SEA Ac
LucA
possa mostror a5
e cA ENc
UUcA """


op="s"
notas=["",""]
boletim=[]

while op.lower()=="s":
    nome=input("Digite o nome: ")
    notas[0]=float(input("Nota 1: "))
    notas[1]=float(input("Nota 2: "))
    op=input("Deseja continuar? (s/n) ")
    media=(notas[0]+notas[1])/2
    aluno=[nome,notas[:],media]
    boletim.append(aluno[:])

print(f'{"No.":<8}{"Nome":<10}{"Média":<8}')
for x,y in enumerate(boletim):
    print(f'{x:<8}{y[0]:<10}{y[2]:<8.2f}')

consulta=input("Deseja consultar as notas? (s/n) ")
while consulta.lower()=="s":
    consulta_numero=int(input("Digita o número do aluno: "))
    print(f'N1={y[consulta_numero][0]:<10}, N2={y[consulta_numero][1]:<10}')
    consulta=input("Deseja consultar mais notas? (s/n) ")