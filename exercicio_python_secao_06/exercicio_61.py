"""
61. Faça um programa que calcule o maior número palíndromo feito a partir do produto de dois números de 3 dígitos.
Ex: O maior palíndromo feito a partir do produto de dois números de dois dígitos é 9009 = 91 * 99.
"""
print("[Descubra o maior número palíndromo feito a partir de dois números de 3 dígitos.]")

nmr1, nmr2 = 999, 999

cdg = True

while cdg:

    rslt = nmr1 * nmr2

    if str(rslt) == str(rslt)[::-1]:
        print(f"\n-O maior número palíndromo a partir de dois números de 3 dígitos é; {nmr1}, {nmr2} = {rslt}.")
        cdg = False
    else:

        nmr1 -= 1
        nmr2 -= 1
