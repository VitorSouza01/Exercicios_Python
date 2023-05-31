"""
11. Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for A,
a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a média ponderada, com
pesos 5, 3 e  2.
"""


def notas_alunos(nota_1, nota_2, nota_3):
    if parametro == 'A' or parametro == 'a':
        media_aritmetica = (nota_1 + nota_2 + nota_3) / 3
        return f"\nA Média Aritmética é: {round(media_aritmetica,2)}"

    elif parametro == 'P' or parametro == 'p':
        media_ponderada = ((nota_1 * 5) + (nota_2 * 3) + (nota_3 * 2)) / (5 + 3 + 2)
        return f"\nA Média Ponderada é: {round(media_ponderada,2)}"


nota_1 = float(input("Digite a Nota 1 do aluno: "))
nota_2 = float(input("Digite a Nota 2 do aluno: "))
nota_3 = float(input("Digite a Nota 3 do aluno: "))

while True:
    print("\nParâmetros:")
    print("Letra 'A': Calcula a Média Aritmética!")
    print("Letra 'P': Calcula a Média Ponderada!")
    parametro = input("\nDigite uma das letras: ")

    if parametro == 'A' or parametro == 'a':
        break

    elif parametro == 'P' or parametro == 'p':
        break

    else:
        print("[Número Informado Inválido! Digite Novamente!]")

print(notas_alunos(nota_1, nota_2, nota_3))
