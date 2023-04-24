op='s'
pessoas=[]
while op.lower()=='s':
    pessoa={'nome':input('Nome: '), 'sexo':input("Sexo (M/F): "), 'idade':int(input('Idade: '))}
    op=input("Continuar? S/N ")
    pessoas.append(pessoa)
print(pessoas)

soma=0
mulheres=[]
print(f"Foram cadastradas {len(pessoas)} pessoas")

for i in pessoas:
    soma+=i['idade']
    if i['sexo'].lower()=="f":
        mulheres.append(i['nome'])

media_idade=soma/len(pessoas)
print(f"A média de idade é: {media_idade} anos")

print(f"Pessoas do sexo Feminino: {mulheres}")

pessoas_acima_media=[]
for i in pessoas:
    if i['idade']>media_idade:
        pessoas_acima_media.append(i['nome'])

print(f"Pessoas com a idade acima da média: {pessoas_acima_media}")