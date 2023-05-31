"""
09. Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro. O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = π * raio² * altura, onde π = 3.141592.
"""


def volume_cilindro(altura, raio):
    return (3.14 * ((raio ** 2) * altura))


altura = float(input("Digite a Altura do cilindro: "))
raio = float(input("Digite o Raio do cilindro: "))
print(f"\nO Volume do cilindro é: {round(volume_cilindro(altura,raio),2)}")
