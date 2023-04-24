def contador():
    print("Contando de 1 a 10")
    for i in range(1,10):
        print(i,end=' ')
    print('')

    print("Contando de 10 a 1")


    for i in range(10,1,-2):
        print(i,end=' ')
    print('')   

    print('Contagem personalizada: ')
    inicio=int(input("Início: "))
    fim=int(input("fim: "))
    passo=int(input("passo: "))

    if passo=='0':
        passo=1
    
    if passo>0 and inicio>fim:
        passo=passo*-1

    for i in range(inicio,fim,passo):
        print(i,end=' ')
    print('')   

contador()