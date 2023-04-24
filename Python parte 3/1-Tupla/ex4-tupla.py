"""
' Daezenvolva um
pro%rumu quaeleia |
quatro valores pelo ;
taclado e guarda-os —
em uma tupla. No final.
Lucoade â
A) Quantas vozas 3
aparecau o valor 9 |
E) Em que posifao foi
diãitudu o primeiro |
valor 3. |
C) Quais Foram os
númearos pares
"""
tupla=(int(input('Digite o primeiro valor: ')),
       int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')),
       int(input('Digite o quarto valor: ')))
print(f"O 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O primeiro 3 está na posição {tupla.index(3)}")
else:
    print(f'O valor 3 não está em nenhuma posição')

print("Números pares:")
for elemento in tupla:
    if(int(elemento) % 2 ==0):
        print(elemento)
