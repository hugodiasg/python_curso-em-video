# import moeda
from utilidades import moeda
from utilidades import dados

moeda.resumo(dados.lerDinheiro("Valor: "),dados.lerDinheiro("Aumento em %: "),dados.lerDinheiro("Diminuição em %: "))
