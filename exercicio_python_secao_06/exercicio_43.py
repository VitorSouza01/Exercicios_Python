"""
43. Faça um programa que leia um número inderteminado de idades de indivíduos (pare quando for informado a idade 0),
e calcule a idade média desse grupo.
"""
print("-Descubra A Idade Média De Um Grupo-")
print("Obs; O código será parado quando digitado 0 ou um número negativo!\n")

codigo = True
idadesoma = 0
media = 0

while codigo:
    idade = int(input("-Digite o valor de uma idade: "))
    idadesoma = idadesoma + idade

    if idade > 0:
        # não sei porque fiz isso mas deu certo
        zero = 0 + 0

    elif idade <=0:
        media = idadesoma / 2
        codigo = False

print(f"\n-A Idade Média Desse Grupo é; {media}.")
