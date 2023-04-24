def metade(valor,formatado=False):
    if formatado==False:
        return valor/2
    else:
        return formatar(valor/2)


def dobro(valor,formatado=False):
    if formatado==False:
        return valor*2
    else:
        return formatar(valor*2)


def aumentar(valor,inc,formatado=False):
    if formatado==False:
        return (valor*(inc+100)/100)
    else:
        return formatar((valor*(inc+100)/100))


def diminuir(valor,inc,formatado=False):
    if formatado==False:
        return ((valor*(100-inc)/100))
    else:
        return formatar((valor*(100-inc)/100))


def formatar(valor):
    return f"R$ {valor:.2f}".replace('.',',')


def resumo(valor,inc,dec):
    print(31*"-")
    print(f'{"RESUMO":^30}')
    print(31*"-")
    print(f"Preço: \t \t {formatar(valor)}")
    print(f"Metade \t \t {metade(valor,True)}")
    print(f"Dobro: \t \t {dobro(valor,True)}")
    print(f"{('+'+str(inc)+'%')}: \t {aumentar(valor,inc,True)}")
    print(f"{('-'+str(dec)+'%')}: \t {diminuir(valor,dec,True)}")
    print(31*"-")
