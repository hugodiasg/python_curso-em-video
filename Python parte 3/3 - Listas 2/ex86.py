""" 

' Cria um programa
que cria uma matriz de
dimensao 3x3 e
preencha com valores
lidos palo teclado.

Disaa u uAda A
matriz na tela. coma
formata£ao correta.
"""

matriz=[]
linha=[]
j=0
i=0
for i in range(3):
    for j in range(3):
        linha.append(float(input(f"Digite o valor {j},{i} :")))
    matriz.append(linha)
    linha=[]
print("Matriz:")
for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]:^5}',end="")
    print()
