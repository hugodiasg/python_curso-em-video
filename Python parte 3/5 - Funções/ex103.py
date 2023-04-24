def campeonato(nome,gols):     # Variável opcional: inicilizar a variável no argumento da função 
    if nome=="":
        nome="<Desconhecido>"
    if gols=="":
        gols="0"
    print(f"O jogador {nome} fez {gols} gols.")

campeonato(input("Nome do jogador: "),input("Quantidade de gols: "))
