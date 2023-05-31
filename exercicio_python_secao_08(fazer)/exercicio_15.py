"""
15. Crie um programa que receba três valores (obrigatoriamente maiores que zero), representando as medidas
dos três lados de um triângulo. Elabore funções para:

    (a) Determinar se eles lados formam um triângulo, sabendo que:
        * O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.

    (b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo sendo que:
        * Chama-se equilátero o triângulo que tem três lados iguais.
        * Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
        * Recebe o nome de escaleno o triângulo que tem o três lados diferentes.
"""


def triangulo(lado_a, lado_b, lado_c):
    if lado_a < (lado_b + lado_c):
        return "\nÉ um Triângulo!"

    elif lado_b < (lado_a + lado_c):
        return "\n um Triângulo!"

    elif lado_c < (lado_a + lado_b):
        return "\nÉ um Triângulo!"


def tipo_triangulo(lado_a, lado_b, lado_c):
    if lado_a == lado_b and lado_a == lado_c and lado_b == lado_c:
        return "É um Triângulo Equilátero!"

    elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
        return "É um Triângulo Escaleno!"

    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        return "É um Triângulo Isósceles!"


loop = True

while loop:
    while True:
        lado_a = float(input("Digite um valor maior que zero do lado A do triângulo: "))
        if lado_a > 0:
            break
        else:
            print("[Número Inválido! Digite Novamente!]")

    while True:
        lado_b = float(input("Digite um valor maior que zero do lado B do triângulo: "))
        if lado_a > 0:
            break
        else:
            print("[Número Inválido! Digite Novamente!]")

    while True:
        lado_c = float(input("Digite um valor maior que zero do lado C do triângulo: "))
        if lado_a > 0:
            break
        else:
            print("[Número Inválido! Digite Novamente!]")

    loop = False

print(triangulo(lado_a, lado_b, lado_c))
print(tipo_triangulo(lado_a, lado_b, lado_c))
