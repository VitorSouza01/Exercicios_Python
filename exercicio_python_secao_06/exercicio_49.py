"""
49. O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu
salário. Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela,
pois está rendendo 2% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo
5% ao mês. Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor
pertencente a João iguale ou ultrapasse o valor pertecente a Carlos. Teste com outros valores para as taxas.
"""
print("O salário de João equivale a um terço do salário de Carlos!")
print("João aplica seu salário em um banco que rende 5% ao mês. Carlos aplica seu salário em um banco que rende 2% "
      "ao mês.")

print("\nDescrubra quantos meses é necessário para o valor do dinheiro no banco do João iguale ou ultrapasse o valor "
      "do primeiro de dinheiro no banco do Carlos")

slr_carlos = float(input("-Digite o valor do salário do Carlos R$; "))
slr_joao = slr_carlos/3

#rendimento mensal de carlos
rdmt_mes_carlos = slr_carlos + ( slr_carlos * (2/100))

#rendimento mensal de joão
rdmt_mes = slr_joao * (5/100)
rdmt_mes_joao = slr_joao + rdmt_mes

cdg = True
nv_rdmt_mes_joao = slr_joao
loop_mes = 0

while cdg:

    if nv_rdmt_mes_joao >= rdmt_mes_carlos:

        print(f"\n-Para o João ultrapassar o valor do salário de Calors (R$ {rdmt_mes_carlos:.2f}) é necessario "
              f"{loop_mes} meses.")
        print(f"-Em {loop_mes} meses, o valor de João é; R$ {nv_rdmt_mes_joao:.2f}.")

        cdg = False

    else:

        nv_rdmt_mes_joao = nv_rdmt_mes_joao + rdmt_mes

        loop_mes = loop_mes + 1
