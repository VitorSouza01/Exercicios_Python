"""
05. Faça uma função e um programa de teste para o cálculo do volume de uma esfera. Sendo que o raio é o passado
por parâmetro.
V = 4 / 3 * π * R3
"""


def volume_esfera(raio):
  return 4 / 3 * (3.14) * raio


raio = float(input("Digite o valor do raio: "))
print(f"\nO volume da esfera do raio é: {volume_esfera(raio)}")
