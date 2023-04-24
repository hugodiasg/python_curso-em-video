'''
' Façra um programa
que leia um número de 0 a 9999
e mostre na tela cada um dos |
digitos separados. —
2 |
Digite um númaro: 1834
unidade: 4 |
dezeno:3 |
centeno:E |
Lilucoes)| |

'''
numero=int(input("Digite um número de 0 a 9999: "))
print(f"Milhares: {numero//1000 % 10}")
print(f"Centenas: {numero//100 % 10}")
print(f"Dezenas: {numero//10 % 10}")
print(f"Unidades: {numero//1 % 10}")