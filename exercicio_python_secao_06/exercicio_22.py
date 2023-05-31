"""
22. Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária
de notas (válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética.
O número de notas com que o aluno pretende efetuar o cálculo não será fornecido ao programa, o qual terminará quando
for introduzido um valor que não seja válido como nota de aprovação.
"""
print("[Média Aritmética Das Notas Entre 10 e 20!]")
print("(Ao digitar os números não correspondente o programa será parado!)\n")

media = 0
loop = 0
nota_fixa = 0
qtd = 1

while True:

    nota = float(input(f"Digite o valor da {qtd}° nota (De 10 a 20): "))

    if 10 <= nota <= 20:
        nota_fixa = nota_fixa + nota
        loop += 1
        qtd += 1

    else:
        print("Valor Informado Inválido!")
        break

if loop >= 1:
    media = nota_fixa / loop
    print(f"\n[A Média Aritmética Das Suas Notas É; {media}].")
