"""
51. Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento de
1,5%. A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça um programa que
determine o salário atual do funcionário.
"""
print("-Um funcionário tem um salário de R$ 2.000, e em 1996 ele recebeu aumento de 1,5%.")
print("-A partir de 1997, os aumentos correspondem ao dobro do ano anterior.")
print("\n-Descubra qual é o salário atual desse funcionário em 2022;")

vlr_inic_func = 2000
aumt_ano = 1.5 / 100

for n in range(1996, 2022):
    visualizar_ano = aumt_ano * 100
    vlr_aumt = vlr_inic_func + (vlr_inic_func * (aumt_ano))
    aumt_ano = aumt_ano * 2
    vlr_inic_func = vlr_aumt

print(
    f"\n-Em pleno 2022, o funcionário estaria com um aumento de {visualizar_ano}%. O salário atual dele é de; "
    f"R${vlr_aumt:.2f}.")
