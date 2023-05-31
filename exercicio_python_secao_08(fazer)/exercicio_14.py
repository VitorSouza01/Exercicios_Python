"""
14. Faça uma função que receba a distancia em Km e a quantidade de litros de gasolina consumidos por um
carro em um percuso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:

CONSUMO     | (Km/l) | MENSAGEM
menor que   |   8    | Venda o carro!
entre       | 8 e 14 | Econômico!
maior que   |   12   | Super econômico!
"""


def gasolina_consumida(distancia, litro):
    consumo = distancia / litro

    if consumo < 8:
        return f"\nVenda o Carro!"

    elif consumo < 14:
        return f"\nEconômico!"

    elif consumo > 12:
        return f"\nSuper Econômico!"


distancia = float(input("Digite o valor da distância do carro percorrida em Km: "))
litro = float(input("Digite a quantidade de litros de gasolina consumido pelo carro: "))

print(gasolina_consumida(distancia, litro))
