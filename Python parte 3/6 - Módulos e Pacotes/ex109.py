import moeda

p=float(input("Digite um valor em R$: "))
print(f"A metade de {moeda.formatar(p)} é {moeda.metade(p, True)}")
print(f"O dobro de {moeda.formatar(p)} é {moeda.dobro(p, True)}")
print(f"Aumentado 20% de {moeda.formatar(p)} é {moeda.aumentar(p, 20, True)}")
print(f"Diminuindo 30% de {moeda.formatar(p)} é {moeda.diminuir(p, 30, True)}")
