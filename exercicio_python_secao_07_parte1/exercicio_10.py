"""
10. Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral
"""

lp = 0
lst_nt = []

while lp < 15:
    lp += 1
    vlr_nt = float(input(f"Digite a nota do {lp}º aluno: "))

    lst_nt.append(vlr_nt)

md_nt = sum(lst_nt) / len(lst_nt)

print(f"\nA média geral dos alunos é: {md_nt}")

