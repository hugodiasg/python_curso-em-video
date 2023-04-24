""" 
L) Crieumprograma |
onde ousuáriopossa |
digitar cinco valores |
numéricos q |
caodaostre-osemumo
fa no na posifao |
corretadeinserfão
(sem usarosortO).
No final. mostra a lista
ordenada na tela. |
 """
lista=[]
for c in range(0,5):
    n=int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("Adicionado ao final da lista.")
    else:
        pos=0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f"Adicionado na posição {pos} da lista.")
                break
            pos +=1
print(f"Lista em ordem crescente sem usar o sort {lista}")
