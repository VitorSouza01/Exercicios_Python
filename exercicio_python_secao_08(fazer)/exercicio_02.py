"""
02. Faça uma função que receba a data atual (dia, mês e ano inteiro) e exiba-a na tela no formato textual
por extenso.
Exemplo: Data> 01/01/2000, Imprimir: 1 de janeiro de 2000.
"""

from datetime import date


def data_por_extenso(mes):

    for i in range(1):
        if mes == 1:
            mes = "janeiro"

        elif mes == 2:
            mes = "fevereiro"

        elif mes == 3:
            mes = "março"

        elif mes == 4:
            mes = "abril"

        elif mes == 5:
            mes = "maio"

        elif mes == 6:
            mes = "junho"

        elif mes == 7:
            mes = "julho"

        elif mes == 8:
            mes = "agosto"

        elif mes == 9:
            mes = "setembro"

        elif mes == 10:
            mes = "outubro"

        elif mes == 11:
            mes = "novembro"

        elif mes == 12:
            mes = "dezembro"

    return mes


data = date.today()
data_br = data.strftime("%d/%m/%y")
dia = data.day
mes = data.month
ano = data.year

print(f"Data atual: {data_br}.")
print(f"Data textual: {dia} de {data_por_extenso(mes)} de {ano}.")
