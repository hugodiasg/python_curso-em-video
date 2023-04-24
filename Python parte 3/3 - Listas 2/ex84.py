""" o Fa£$a um programa
queleia nome e peso
de várias pessoas,
guardando tudo em
uma lista. No final,
Luciide

A) Quantas pessoos
foram cadastradas.
E) Uma listagem com az
passoas mais
pesados,

£) Uma listagem com as
passoas mais lovos.
 """

cadastro=[]
maiores_pesos=[]
menores_pesos=[]
menor_peso=maior_peso=0
contador=0
op=""
while op.lower() != "n":
    pessoa_peso=[input("Digite o nome: "),float(input("Digite o peso: "))]

    if  contador==0 or pessoa_peso[1]>maior_peso:
        maior_peso=pessoa_peso[1]
    
    if contador==0 or pessoa_peso[1]<menor_peso:
        menor_peso=pessoa_peso[1]

    cadastro.append(pessoa_peso[:])
    del pessoa_peso
    contador +=1
    op=input("Deseja continuar? S/N ")

for elemento in cadastro:
    if elemento[1] == maior_peso:
        maiores_pesos.append(elemento[0])

    if elemento[1] == menor_peso:
        menores_pesos.append(elemento[0])

print(f"Foram cadastradas {len(cadastro)} pessoas")
print(f"O maior peso é {maior_peso}kg e quem tem ele é: {maiores_pesos}")
print(f"O menor peso é {menor_peso}kg e quem tem ele é: {menores_pesos}")