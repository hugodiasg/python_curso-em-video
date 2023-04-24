def fatorial(n=0):     # Variável opcional: inicilizar a variável no argumento da função 
    """
    DESCRIÇÃO DA FUNÇÃO (doc string)
    param n = número do fatorial
    """
    f=1
    for c in range(n,0,-1):
        f *=c
    return f


help(fatorial)
print(f"Fatorial de vazio: {fatorial()}")
print(f"Fatorial de 10: {fatorial(4)}")