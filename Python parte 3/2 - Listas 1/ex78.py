""" 
O Fasaum programa:
qua leia 5 valores |
numéricos guarde |
os em uma lista. |
No final; mostre qual
foi omaior gomenor
valordigitadocas
suas respectivas |
posifaas nalista. |

 """
lista=[1,8,1,6,8]
# lista=float(input("Digite o primeiro número: ")),float(input("Digite o segundo número: ")),float(input("Digite o terceiro número: ")),float(input("Digite o quarto número: ")),float(input("Digite o quinto número: "))]
print(f"Lista: {lista}")
texto_maior=f'Maior valor é {max(lista)} na posição: '
texto_menor=f'Menor valor é {min(lista)} na posição: '
for posicao, valor in enumerate(lista):
    if valor==max(lista):
        texto_maior+=str(posicao)+", " 
    if valor==min(lista):
        texto_menor+=str(posicao)+", "

print(texto_maior)
print(texto_menor)