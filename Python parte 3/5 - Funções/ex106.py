def chamarHelp(funcao): 
    while funcao.strip().lower()!="fim":
        print(f"Acessando o help da função {funcao}...")
        help(funcao)
        funcao=input("Digite outra função: ")
    print("Finalizando o chamarHelp()...")
chamarHelp(input("Acessar o manual da função: "))




