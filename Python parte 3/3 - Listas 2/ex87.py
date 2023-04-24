""" 

' Aprimora o dezafio
aaA ccA dA Lc
no final:

A)Asoma da todos os5
valores poras

Ec dLc

B) A soma dos valoras
da terceira coluna.
maior valor 
segunda linha.
"""

matriz=[]
linha=[]
j=0
i=0
soma_par=0
soma_3col=0

for i in range(3):
    for j in range(3):
        cell=float(input(f"Digite o valor {j},{i} :"))
        linha.append(cell)

        if cell%2==0:
            soma_par=soma_par+cell

        if j==2:
            soma_3col=soma_3col+cell
        if i==1:
            if j==0 or cell>maiorvalor2linha:
                maiorvalor2linha=cell
            


    matriz.append(linha)
    linha=[]

print("Matriz:")
for linha in matriz:
    print(*linha, sep="\t")

print(f"Soma dos valores pares: {soma_par}")
print(f"Soma dos valores da terceira coluna é: {soma_3col}")
print(f"Maior valor da segunda linha: {maiorvalor2linha}")


