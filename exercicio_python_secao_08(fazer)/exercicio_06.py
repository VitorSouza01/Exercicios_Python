"""
06. Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos e segudos,
e os converta em segundos.
"""


def converta_segundos(horas, minutos, segundos):
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos


horas = int(input("Digite o valor das Horas: "))
minutos = int(input("Digite o valor dos Minutos: "))
segundos = int(input("Digite o valor dos segundos: "))

print(f"\nOs horários convertido em segundo e somados equivale á: {(converta_segundos(horas, minutos, segundos))} "
      f"segundos.")

