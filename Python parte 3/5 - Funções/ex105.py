def boletim(*notas, sit=False): 
    """
    -> Função para analisar a situação dos alunos
    :param notas: recebe uma ou mais notas
    :para sit: se True, então mostra a situação da turma
    :return: retorna um dicionário com a quantidade de notas, a média,
    a maior nota, a menor nota e a situação da turma (se sit=True).
    """  
    soma=0
    for i,nota in enumerate(notas):
        if i==0 or nota>maior:
            maior=nota
        if i==0 or nota<menor:
            menor=nota
        soma+=nota
    media=soma/len(notas)
    if sit==False:
        return {'Total':len(notas),'Maior':maior,'Menor':menor,'Média':media}
    else:
        if media>=7:
            situacao="Boa"
        elif media>=5:
            situacao="Razoável"
        else:
            situacao="Ruim"
        return {'Total':len(notas),'Maior':maior,'Menor':menor,'Média':media,'Situacao':situacao}

help(boletim)
print(boletim(6,7,1,sit=True))




