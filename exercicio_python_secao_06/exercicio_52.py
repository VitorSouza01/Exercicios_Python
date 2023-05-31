"""
52. Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco
e retorne quantas notas de cada valor serão necessárias para atender ao saque com a manor quantidade
de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""
print("[Descubra quantas notas de cada valor será necessário para o saque!]")
print("[Notas disponíveis: R$100, R$50, R$20, R$10, R$5, R$2, R$1.]")

vlr_saq0 = int(input("\n-Digite o Valor do Saque(Valor inteiro!);"))

vlr_saq = vlr_saq0

cdg = True

while cdg:

    # nt... -> Nota
    # sbr... -> Sobra

    if vlr_saq >= 100:
        nt100 = vlr_saq // 100
        sbr100 = vlr_saq % 100
        vlr_saq = sbr100
    else:
        nt100 = 0

    if vlr_saq >= 50:
        nt50 = vlr_saq // 50
        sbr50 = vlr_saq % 50
        vlr_saq = sbr50
    else:
        nt50 = 0

    if vlr_saq >= 20:
        nt20 = vlr_saq // 20
        sbr20 = vlr_saq % 20
        vlr_saq = sbr20
    else:
        nt20 = 0

    if vlr_saq >= 10:
        nt10 = vlr_saq // 10
        sbr10 = vlr_saq % 10
        vlr_saq = sbr10
    else:
        nt10 = 0

    if vlr_saq >= 5:
        nt5 = vlr_saq // 5
        sbr5 = vlr_saq % 5
        vlr_saq = sbr5
    else:
        nt5 = 0

    if vlr_saq >= 2:
        nt2 = vlr_saq // 2
        sbr2 = vlr_saq % 2
        vlr_saq = sbr2
    else:
        nt2 = 0

    if vlr_saq >= 1:
        nt1 = vlr_saq // 1
        sbr1 = vlr_saq % 1
        vlr_saq = sbr1
    else:
        nt1 = 0

    cdg = False

print(f"\n[As notas do saque de R${vlr_saq0} são: ]")
print(f"[{nt100} notas de R$100.]")
print(f"[{nt50} notas de R$50.]")
print(f"[{nt20} notas de R$20.]")
print(f"[{nt10} notas de R$10.]")
print(f"[{nt5} notas de R$5.]")
print(f"[{nt2} notas de R$2.]")
print(f"[{nt1} notas de R$1.]")
