def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError,TypeError):
            print("Digite um número válido.")
            continue
        except KeyboardInterrupt:
            print("Programa interrompido pelo usuário.")
            return 0
        else:
            # print(f"O valor digitado foi: {num}")
            return num

def linha(tam=42):
        return "-"*tam

def cabecalho(txt,tam=42):
    print(linha(tam))
    print(txt.center(tam))
    print(linha(tam))

def opcoes(lista):
      c=1
      for item in lista:
            print(f"{c} - {item}")
            c+=1
def menu(txt,tam=42,lista=[]):
      cabecalho(txt,tam)
      opcoes(lista)
      print(linha(tam))
      opcao_escolhida=leiaInt("Opção: ")
      return opcao_escolhida