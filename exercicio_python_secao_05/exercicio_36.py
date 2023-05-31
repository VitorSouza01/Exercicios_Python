"""
36. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor.
Para calcular a comissão, considere a tabela abaixo:

VENDA MENSAL                                            |   COMISÃO
Maior ou igual a R$100.000,00                           |R$700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R$80.000,00   |R$650,00 + 14% das vendas
Menor que R$80.000,00 e maior ou igual a R$60.000,00    |R$600,00 + 14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00    |R$550,00 + 14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00    |R$500,00 + 14% das vendas
Menor que R20.000,00                                    |R$400,00 + 14% das vendas
"""

print("[ DESCUBRA A SUA COMISSÃO ]")
venda = float(input("-Digite o valor de venda;"))

if venda < 20000:
    print(f"\nA comissão do valor de {venda} será;[{int(venda*0.14)+400}].")

elif 20000 >= venda < 40000:
    print(f"\nA comissão do valor de {venda} será:[{int(venda*0.14)+500}].")

elif 40000 >= venda < 60000:
    print(f"\nA comissão do valor de {venda} será:[{int(venda*0.14)+550}].")
elif 60000 >= venda < 80000:
    print(f"\nA comissão do valor de {venda} será:[{int(venda*0.14)+600}].")
elif 80000 >= venda < 100000:
    print(f"\nA comissão do valor de {venda} será:[{int(venda*0.14)+650}].")
elif venda > 100000:
    print(f"\nA comissão do valor de {venda} será:[{int(venda*0.16)+700}].")
