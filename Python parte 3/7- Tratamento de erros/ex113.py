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

x=leiaInt("Digite um valor: ")
print(f"Número digitado foi: {x}")