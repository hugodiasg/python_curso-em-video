""" Fa£Fa um programa
queae leia nome e média
dae um aluno.
quardando também a
situafão em um
dicionário. No final,
mostre o conteúdo da
estrutura na tala.
 """

boletim={'nome':input("Digite o nome: "),'media':float(input("Digite a média: "))}
print(f"O nome: {boletim['nome']}")
print(f"A média: {boletim['media']}")
if (boletim['media']>=7):   
    print("Situação: aprovado.")
else:
    print("Situação: reprovado.")
