'''
' Cria um programa
que leia o nome de uma
cidade e diga se ela
coma£sa ou não como
nome "“SANTO”,

'''
cidade=input("Digite nome da sua cidade: ")
print(f"Sua cidade começa com Santo? {'SANTO' in cidade.split()[0].upper()}")
