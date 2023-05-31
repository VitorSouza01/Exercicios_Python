"""
04. Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado perfeito é um número inteiro
não negativo que pode ser expresso como o quadrado de outro número inteiro. Ex: 1, 4, 9...
"""


def quadrado_perfeito(raiz_q):
    raiz_q = numero ** (1 / 2)

    if (raiz_q ** 2) == numero:
        return f"\nO número {numero} é um quadrado perfeito!"

    else:
        return f"\nO número {numero} não é um quadrado perfeito!"


numero = int(input("Digite um número: "))
print(quadrado_perfeito(numero))
