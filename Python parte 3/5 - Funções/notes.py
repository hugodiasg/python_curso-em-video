def contador(*num):
    print(f"Recebi {len(num)} valores: {num}")
    print(f"O num empacotado é um {type(num)}")

print("Declarar uma função que receba n parâmetros de quantidade arbitrária")
print("Chamando a função contador()")
contador(1,2,3,4)

print("Para trabalhar com uma lista como parâmetro, pode-se colocar contador(lista)")
