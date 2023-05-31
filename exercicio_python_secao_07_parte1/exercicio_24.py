"""
24. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o
segundo representando a sua altura em metros. Encontre o aluno mais baixo e o mais alto. Mostre o número
do aluno mais baixo e do mais alto, justamente com suas alturas.
"""

nmr_aln = []
alt_aln = []

for i in range(10):
    vlr_nmr = int(input(f"Informe o número do {i+1}º aluno: "))
    nmr_aln.append(vlr_nmr)
    vlr_alt = float(input(f"Informe a altura do {i+1}° aluno: "))
    alt_aln.append(vlr_alt)


aln_bax_alt = min(alt_aln)
aln_bax_nmr = nmr_aln[(alt_aln.index(aln_bax_alt))]

aln_aut_alt = max(alt_aln)
aln_aut_nmr = nmr_aln[(alt_aln.index(aln_aut_alt))]


print(f"\n[Aluno Mais Baixo]")
print(f"Número do aluno: {aln_bax_nmr}. Altura do aluno: {aln_bax_alt}.")

print(f"\n[Aluno Mais Alto]")
print(f"Número do aluno: {aln_aut_nmr}. Altura do aluno: {aln_aut_alt}.")

