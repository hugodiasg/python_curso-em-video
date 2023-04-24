def leiaInt(texto):   
    n=input(texto)
    while not n.isnumeric():
        n=input("Isso não é um número, digite novamente: ")
    return n
        


numero =leiaInt("Digite um número: ")
print(f"O número digitado foi {numero}")



