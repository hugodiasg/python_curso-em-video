""" 
LAST programa |
onde o usuáriopossa |
digitar vários valores
numéricos q |
cadaostre-osemuma =
lista. Caso o número já
axistaládentro.ele |
nao será adicionado.
No final. serão |
axibidos todos os |
valores únicos 3
digitados. emordem =
crescento, |
 """
lista=[]
op="s"
while op.lower()=="s":
    n=int(input("Digite um número: "))
    if n in lista:
        print("Valor duplicado não adicionado")
    else:
        lista.append(n)
    op=input("Deseja continuar? S/N ")
print(f"A lista digitada é: {lista}")
lista.sort()
print(f"Ordenando: {lista}")