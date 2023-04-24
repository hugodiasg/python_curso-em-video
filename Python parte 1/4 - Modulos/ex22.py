'''
' Crie um programa
quea leia o nomae |
completo da uma |
passoa a mostra: |
» Onoma com todas as
latras maiúsculas |
» Onomea com todas
minúsculas. |
» Quantasletrasão —
todo (sem considerar:
aspasos). |
» Quantas latras temo
primairo noma. |

'''
nome_completo=input("Digite seu nome completo: ")
print(f"Nome completo: {nome_completo}")
print(f"Com todas as letras maiúsculas: {nome_completo.upper()}")
print(f"Com todas as letras minúsculas: {nome_completo.lower()}")
print(f"Quantidade de letras sem espaço: {len(nome_completo)-nome_completo.count(' ')}")
print(f"Quantidade de letras no primeiro nome: {len(nome_completo.split()[0])}")