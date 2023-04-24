from lib.interface import cabecalho

def arquivoExiste(nome):
    try:
        arq=open(nome,'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a=open(nome,'wt+')
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"Arquivo {nome} criado com sucesso.")
    finally:
        a.close()

def lerArquivo(nome):
    try:
        arq=open(nome,'rt')
    except:
        print("Erro ao ler arquivo.")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        # print(arq.read())
        for linha in arq:
            dado=linha.split(";")
            dado[1]=dado[1].replace("\n","")
            print(f'{dado[0]:<30} {dado[1]:>3.3} anos')
    finally:
        arq.close()

def cadastrar(arq,nome="Desconhecido",idade=0):
    try:
        a=open(arq,'at')
        print("Registro adicionado.")
    except:
        print("Erro ao abrir arquivo.")
    else:
        cabecalho("CADASTRO DE PESSOAS")
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Erro ao registrar pessoas no arquivo.")
        finally:
            a.close()