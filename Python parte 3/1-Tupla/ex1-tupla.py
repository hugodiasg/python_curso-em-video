"""
    Crie um programa que trenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

    Seu programa deverá ler um número pelo usuário e mostrá-lo por extenso
"""
zero_a_vinte=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


entre_0_e_20=True
while entre_0_e_20:
    numero=input("Informe um número de 0 a 20: ")
    numero_int=int(numero)
    entre_0_e_20=numero_int<0 or numero_int>20
print(f"O seu número {numero} por extenso é {zero_a_vinte[numero_int]}.")