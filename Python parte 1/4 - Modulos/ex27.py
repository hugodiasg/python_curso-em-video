'''
' Fafaumprograma
que leia o noma |
completo de uma ;
paessoo. mostrando em
seguida o primeiroao —
último nome |
seporodomente. ;
Ex: AnaMaria deSouza |
primairo = Ana |
último = Souza |
'''
nome=input("Digite um nome: ").strip().split()
print(f"Primeiro nome: {nome[0]}")
print(f"Último nome: {nome[len(nome)-1]}")
