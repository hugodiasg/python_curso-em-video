import moeda

p=float(input("Digite um valor em R$: "))
print(f"A metade de {moeda.formatar(p)} é {moeda.formatar(moeda.metade(p))}")
print(f"O dobro de {moeda.formatar(p)} é {moeda.formatar(moeda.dobro(p))}")
print(f"Aumentado {moeda.formatar(10)} de {moeda.formatar(p)} é {moeda.formatar(moeda.aumentar(p, 10))}")
print(f"Diminuindo {moeda.formatar(5)} de {moeda.formatar(p)} é {moeda.formatar(moeda.diminuir(p, 5))}")
