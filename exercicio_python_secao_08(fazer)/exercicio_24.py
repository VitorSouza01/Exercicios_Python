"""
24. Escreva uma função que gera um triângulo de altura e lados n e base 2*n-1.
Por exemplo, a saída para n=6 seria:
     *
    ***
   *****
  *******
 *********
***********
"""


def triangulo(numero):
    base = 2 * numero - 1

    for i in range(numero):

        for n in range(numero-i-1):
            print(" ", end="")

        for n in range(2*i+1):
            print("*", end="")
        print()


numero = int(input("Digite um número que seja a altura do triângulo: "))
triangulo(numero)
