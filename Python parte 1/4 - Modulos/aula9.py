'''
    Manipulação de Texto
'''

#   Fatiamento de strings pulando de 2 em 2
texto="Curso em vídeo Python"
print(f"texto COMPLETO-> {texto}")
print(f"texto[9:21:2] pulando de 2 em 2-> {texto[9:21:2]}")
print(f"texto[:5] do começo a um ponto específico-> {texto[:5]}")
print(f"texto[9::3] do 9 até o final, de 3 em 3-> {texto[9::3]}")
print("Utilizando o replace Curso por Nada -> {}".format(texto.replace('Curso','Nada')))
print('Título -> {} '.format(texto.title()))
print('Captalizado -> {}'.format(texto.capitalize()))
texto2="   Curso em vídeo Python  "
print("Texto com espaços -> {}".format(texto2))
print("Limpando os espaços -> {}".format(texto2.strip()))
print("Limpando os espaços somente À ESQUERDA-> {}".format(texto2.lstrip()))
print("Separando as palavras dentro de uma string -> {}".format(texto.split()))
print("Juntando elementos em uma string separado por '-' -> {}".format('-'.join(texto.split())))