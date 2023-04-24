def lerDinheiro(msg):
    valido=False
    while not valido:
        ent=str(input(msg)).replace(',','.').strip()
    
        if ent.isalpha() or ent=="":
            print(f"ERRO: \'{ent}\' é um preco inválido, digite novamente: ")
        else:
            # print("Dado válido")
            valido=True
            return float(ent)