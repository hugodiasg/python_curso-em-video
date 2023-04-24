"""
' Crie um programa |
que tenha uma tupla |
únicacomnomesde
produtos e seus ;
raspectivos prafos, -
na sequéncia. |
No final. mostreuma |
listagemdeprafos. =
organizando 05 dados
em forma tabular. |
"""
n1=input('Digite o primeiro valor: ')
n2=input('Digite o segundo valor: ')
n3=input('Digite o terceiro valor: ')
n4=input('Digite o quarto valor: ')
tupla=(n1,n2,n3,n4)
print(f"O 9 apareceu {tupla.count('9')} vezes")
if tupla.count('3')>0:
    print(f"O primeiro 3 está na posição {tupla.index('3')}")
else:
    print(f'O valor 3 não está em nenhuma posição')

print("Números pares:")
for elemento in tupla:
    if(int(elemento) % 2 ==0):
        print(elemento)
