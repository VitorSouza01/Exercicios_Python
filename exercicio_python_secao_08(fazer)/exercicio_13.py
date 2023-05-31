"""
13. Faça uma função que receba dois valores numéricos e um símbolo. Este símbolo representará a operação que
se deseja efetuar com os números. Se o símbolo for + deverá ser realizada uma adição, se for - uma subtração,
se fpr / uma divisão e se for * será efetuada uma multiplicação.
"""


def operacao_matematica(numero_1, numero_2, simbolo):
    if simbolo == '+':
        adicao = numero_1 + numero_2
        return f"{numero_1} + {numero_2} = {adicao}."

    elif simbolo == '-':
        subtracao = numero_1 - numero_2
        return f"{numero_1} - {numero_2} = {subtracao}."

    elif simbolo == '/':
        divisao = numero_1 / numero_2
        return f"{numero_1} / {numero_2} = {divisao}."

    elif simbolo == '*':
        multiplicacao = numero_1 * numero_2
        return f"{numero_1} * {numero_2} = {multiplicacao}."


numero_1 = float(input("Digite o valor do Número 1: "))
numero_2 = float(input("Digite o valor do Número 2: "))

while True:
    print("\n[OPERAÇÕES DISPONÍVEIS]")
    print("| [Adição] = + | [Subtração] = - | [Divisão] = / | [Multiplicação] = * |")
    simbolo = str(input("Digite o símbolo correspondente da operação: "))

    if simbolo == '+' or simbolo == '-' or simbolo == '/' or simbolo == '*':
        break

    else:
        print("[Número Inválido! Digite Novamente!]")

print(operacao_matematica(numero_1, numero_2, simbolo))
