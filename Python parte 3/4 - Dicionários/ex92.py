""" ' Crie um programa
quea leia nomea,. ano de
nascimento e carteira
dae trabalho e
cadastre-os (com
idade) em um dicionário
sa por acaso a CTPS
for diferente de ZERO,
o dicionário rceceberá
também o ano de
contratafao a o
salário. Calcule e
acrescenta, além da
idade. com quantos
anos a pessoa voi s5e
aposeantar. """
from datetime import date

cadastro={'nome':input('Nome: '),'nascimento':int(input("Ano de nascimento: ")),
          'carteira_trabalho':int(input("Carteira de Trabalho (0 - Sem carteira): "))
          }
cadastro['idade']=datetime.now().year-cadastro['nascimento']

if (cadastro['carteira_trabalho']!=0):
    cadastro['ano_contratacao']=int(input("Ano da contratação: "))
    cadastro['salario']=int(input("Salário: "))
    cadastro['ano_aposentar']= cadastro['ano_contratacao']+20
    cadastro['idade_aposentar']=cadastro['ano_aposentar']-cadastro['nascimento']
    if cadastro['idade_aposentar']>=75:
        cadastro['idade_aposentar']=75
        cadastro['ano_aposentar']= cadastro['nascimento']+75
    
    print(f"Você vai se aposentar em {cadastro['ano_aposentar']} e terá {cadastro['idade_aposentar']} anos.")