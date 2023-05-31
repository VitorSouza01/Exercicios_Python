"""
31. Faça um programa que receba a altura e o peso de uma pessoa.
De acordo com a tabela a seguir, verifique e mostra qual a classificação dessa pessoa;

|       Altura     |    Peso até 60     |   Peso entre 60 e 90 (Inclusive)  |   Acima de 90 |
|   Menor que 1,20 |        A           |               E                   |       G       |
|   De 1,20 a 1,70 |        B           |               D                   |       H       |
|   Maior que 1,70 |        C           |               E                   |       I       |
"""

print("-Descubra sua classificação sobre peso e altura!")

altura = float(input("Digite a sua altura:"))
peso = float(input("Digite o seu peso:"))

if altura < 1.20 and peso < 60:
    print(f"\nA sua classificação é: [A].")
elif altura < 1.70 and peso < 60:
    print(f"\nA sua classificação é: [B].")
elif altura >= 1.70 and peso < 60:
    print(f"\nA sua classificação é: [C].")
elif altura < 1.20 and peso < 90:
    print(f"\nA sua classificação é: [D].")
elif altura < 1.70 and peso < 90:
    print(f"\nA sua classificação é: [E].")
elif altura >= 1.70 and peso < 90:
    print(f"\nA sua classificação é: [F].")
elif altura < 1.20 and peso >= 90:
    print(f"\nA sua classificação é: [G].")
elif altura < 1.70 and peso >= 90:
    print(f"\nA sua classificação é: [H].")
elif altura >= 1.70 and peso >= 90:
    print(f"\nA sua classificação é: [I].")
