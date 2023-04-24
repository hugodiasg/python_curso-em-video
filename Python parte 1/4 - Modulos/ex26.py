'''
' Faça um programa
quea leia uma frase palo:
teclado a mostra: |
» Quantas vezas
aparece a letra "A" -

» Em qua posifão ela
apareca a primeira |
vaz. í

» Em que posifao ela
— apareca última vez.
'''
frase=input("Digite uma frase: ").strip
print(f"Quantas vezes aparece a letra A: {frase.count('A')}")
print(f"Posição da primeira aparição: {frase.find('A')+1}")
print(f"Posição da última aparição: {frase.rfind('A')+1}")
