"""
60. Faça um programa que leia vários números, calcule e mostre:

    (a) A soma dos números digitados
    (b) A quantidade de números digitados
    (c) A média dos números digitados
    (d) O maior número digitado
    (e) O menor número digitado
    (f) A média dos números pares

Finalize a entrada de dados caso o usuário informe o valor 0.
"""
print("[Programa que calcula vários números!]")

# (a) A soma dos números digitados
# (b) A quantidade de números digitados
# (c) A média dos números digitados
# (d) O maior número digitado
# (e) O menor número digitado
# (f) A média dos números pares
a, b, c, d, f, cdg = 0, 0, 0, 0, 0, 0

qtdd_nmr = int(input("\n-Digite a quantidade de números que será introduzido no programa; "))

for n in range(1, qtdd_nmr + 1):

    nmr = int(input(f"\n-Digite o valor do {n} número: "))

    if cdg == 0:
        e = nmr

    # soma
    a += nmr

    # quantidade
    b += 1

    # media
    c += nmr

    # maior
    if nmr > d:
        d = nmr

    # menor
    if nmr < e:
        e = nmr

    # media pares
    if (nmr % 2) == 0:
        f += nmr

    cdg = 1

print(f"\n-A soma dos números digitados; {a}.")
print(f"-A quantidade de números digitados; {b}.")
print(f"-A média dos números digitados; {c / 2}.")
print(f"-O maior número digitado; {d}.")
print(f"-O menor número digitado; {e}.")
print(f"A média dos números pares; {f / 2}.")
