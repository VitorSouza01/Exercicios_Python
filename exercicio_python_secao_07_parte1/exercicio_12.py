"""
12. Fazer um programa para ler 5 valores, em seguida, mostrar todos
os valores lidos juntamente como o maior, o menor e a média dos valores.
"""

print("Digite 5 valores;\n")

lp = 0
lst = []

while lp < 5:
    lp += 1
    vlr = float(input(f"Digite o {lp}º valor: "))
    lst.append(vlr)

md = sum(lst) / len(lst)

print(f"\nTodos valores: {lst}")
print(f"Maior valor: {max(lst)}")
print(f"Menor valor: {min(lst)}")
print(f"Média dos valores: {md}")

