""" 
o Cria um programa
onda o usuário digite
uma expressao
qualquer que use
parêéntazas. Seu
aplicativo deverá
analizar se q
expressao passado
astácomos
parênteses abertos e
Fachados na ordem
correta,
 """
expressao=input("Digite uma expressão matemática: ")
n_parentesis_abrindo=expressao.count("(")
n_parentesis_fechando=expressao.count(")")
if n_parentesis_abrindo == n_parentesis_fechando:
    print("Expressão válida")
else:
    print(f"Expressão inválida, há {n_parentesis_fechando} ')' e {n_parentesis_abrindo} '(' ")