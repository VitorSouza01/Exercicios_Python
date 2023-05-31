"""
13. Fazer um programa para ler 5 valores, e em seguida, mostrar a
posição onde se encontram o maior e o menor número.
"""


print("Digite 5 valores;\n")

lp = 0
lst = []

while lp < 5:
    lp += 1
    vlr = float(input(f"Digite o {lp}º valor: "))
    lst.append(vlr)

vlr_mr = max(lst)
vlr_mn = min(lst)

print(f"\nTodos valores: {lst}")

print(f"\nMaior valor: {vlr_mr}")
print(f"Posição do maior valor: {lst.index(vlr_mr)}")

print(f"\nMenor valor: {vlr_mn}")
print(f"POsição do menor valor: {lst.index(vlr_mn)}")


