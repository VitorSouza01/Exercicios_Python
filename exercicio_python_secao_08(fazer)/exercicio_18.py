"""
18. Faça uma função que receba por parâmetro dois valores x e Y. Calcule e retorne o resultado de Xz para o
programa principal. Atenção não utilize nenhuma função pronta de exponenciação.
"""


def parametro(valor_x, valor_y):
    return f"O resultado de Xz é: {valor_x ** valor_y}"


valor_x = float(input("Digite o Valor de X: "))
valor_y = float(input("Digite o Valor de Y: "))

print(parametro(valor_x, valor_y))
