from lib.interface import *
from lib.arquivo import *


arquivo="cadastro.txt"

if arquivoExiste(arquivo):
    print("Arquivo encontrado com sucesso.")
else:
    print("Arquivo não encontrado.")
    criarArquivo(arquivo)

while True:
    resposta = menu("MENU PRINCIPAL",30,["Ver pessoas cadastradas.","Cadastrar nova pessoa.","Sair do sistema."])
    
    match resposta:
        case 1:
            print("Pessoas cadastradas: ")
            print(lerArquivo(arquivo))
        case 2:
            print("Cadastro de pessoas")
            cadastrar(arquivo,input("Digite um nome: "),leiaInt("Digite a idade: "))
        case 3:
            print("Saindo do sistema")
            break
        case _:
            print("ERRO: Digite uma opção válida")

