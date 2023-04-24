lista=['a','b','c','d']
print(f'A lista é: {lista}')

lista.append("ee")
print(f'Adicionando um último elemento: {lista}')

lista=['a','b','c','d']
lista.insert(2,"ee")
print(f'Adicionando em outra posição: {lista}')

lista=['a','b','c','d']
del lista[3]
print(f'Deletando pelo índice: {lista}')

lista=['a','b','c','d']
lista.pop(3)
print(f'Deletando pelo índice (opção 2): {lista}')

lista=['a','b','c','d']
lista.remove('c')
print(f'Deletando pelo conteúdo: {lista}')

lista=list(range(2,6))
print(f'Criando lista com números ordenados: {lista}')

lista=[5,2,3,6,7,1]
print(f'Lista em ordem aleatória: {lista}')
lista.sort()
print(f'Ordem crescente: {lista}')
lista.sort(reverse=True)
print(f'Ordem decrescente: {lista}')

for posicao, valor in enumerate(lista):
    print(f'Na posição {posicao}, encontrei o valor {valor}')

print(f'OBS.: Quando se faz Lista1 = Lista2, está se fazendo uma ligação e não uma cópia. Qualquer mudança em uma delas, muda as duas')
print(f'Para fazer uma cópia, deve-se fazer Lista1 = Lista2[:].')

lista=[5,2,3,6,7,1]
print(lista)
print(f'Valor [0] da lista: {lista[0]}')
print(sorted(lista))