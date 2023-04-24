from random import randint
def maior(*vetor):

    print('-'*30)
    print(f"{'Maior':^30}")
    print('-'*30)

    print(f"Vetor: {vetor}")
    if (len(vetor)==0):
        print("Nenhum valor foi informado")
    else:
        print(f"Foram informados {len(vetor)} valores")
        maior_valor=0
        for indice,n in enumerate(vetor):
            if indice==1 or n>maior_valor:
                maior_valor=n
        print(f"Maior valor: {maior_valor}")


maior()

maior(randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))

maior(randint(0,100),randint(0,100))

maior(randint(0,100))