import moeda

p=float(input("Digite um valor em R$: "))
print(f"A metade de R$ {p} é R$ {moeda.metade(p):.2f}")
print(f"O dobro de R$ {p} é R$ {moeda.dobro(p):.2f}")
print(f"Aumentado 10 de R$ {p} é R$ {moeda.aumentar(p, 10):.2f}")
print(f"Diminuindo 5 de R$ {p} é R$ {moeda.diminuir(p, 5):.2f}")
