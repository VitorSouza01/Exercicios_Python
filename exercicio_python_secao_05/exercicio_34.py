"""
34. Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela abaixo, quando o
aluno tem mais de 20 faltas ocorre uma redução de conceito.

NOTA         |  CONCEITO (ATÉ 20 FALTAS) | CONCEITO (MAIS DE 20 FALTAS) |
9.0 até 10.0 |          A                |              B               |
7.5 até 8.9  |          B                |              C               |
5.0 até 7.4  |          C                |              D               |
4.0 até 4.9  |          D                |              E               |
0.0 até 3.9  |          E                |              E               |
"""

print("[Descubra o Seu Conceito!]")
nota = float(input("-Digite o valor da sua nota;"))
falta = int(input("-Digite a quantidade de faltas;"))

if falta <= 20:
    if nota <= 3.9:
        print("\nSeu Conceito é;[E]")

    elif nota <= 4.9:
        print("\nSeu Conceito é;[D]")

    elif nota <= 7.4:
        print("\nSeu Conceito é;[C]")

    elif nota <= 8.9:
        print("\nSeu Conceito é;[B]")

    elif nota <= 10:
        print("\nSeu Conceito é;[A]")


elif falta > 20:
    if nota <= 3.9:
        print("\nSeu Conceito é:[E]")

    elif nota <= 4.9:
        print("\nSeu Conceito é:[E]")

    elif nota <= 7.4:
        print("\nSeu Conceito é:[D]")

    elif nota <= 8.9:
        print("\nSeu Conceito é:[C]")

    elif nota <= 10:
        print("\nSeu Conceito é:[B]")

