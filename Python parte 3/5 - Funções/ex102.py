def fatorial(n=0,show=False):     # Variável opcional: inicilizar a variável no argumento da função 
    """
    n = número do fatorial
    show = true para mostrar o cálculo
    return = o valor do fatorial de n
    """
    f=1
    if show==False:
        for c in range(n,0,-1):
            f *=c
        return f
    else:

        for c in range(n,0,-1):
            f *=c
            if c==1:
               print(f"{c} = ",end='') 
            else:
                print(f"{c} x ",end='')
        return f

help(fatorial)
print("Fatorial com o show=True")
print(fatorial(10,True))
print("Fatorial com o show=False")
print(fatorial(10))

