def voto(ano):     
    # Definir a biblioteca somente dentro da função, pois só aqui que ela é utilizada
    from datetime import date
    idade = date.today().year-ano
    if idade<16:
        return f'Com {idade} anos: não vota.'
    elif idade>=16 and idade<18 or idade>65:
        return f'Com {idade} anos: voto opcional.'
    else:
         return f'Com {idade} anos: voto obrigatório.'

print(voto(2005))
print(voto(2018))
print(voto(1950))
print(voto(2007))

