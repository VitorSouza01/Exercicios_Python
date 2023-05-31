"""
40. O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor,
e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo.
Leia o custo de fábrica e escreva o custo ao consumidor.

CUSTO DE FÁBRICA              | % DO DISTRIBUIDOR | % DOS IMPOSTOS |
até R$12.000,00               |         5         |      isento    |
entre R$12.000,00 e 25.000,00 |         10        |        15      |
acima de R$25.000,00          |         15        |        20      |
"""
print("[DESCUBRA O CUSTO DO CARRO AO CONSUMIDOR]")
valor_fabrica = float(input("-Custo do carro de fábrica: "))

if valor_fabrica <= 12000:
    print(f"\nO valor do custo final do carro aplicado comissão e impostos é: "
          f"[R${(valor_fabrica + (valor_fabrica * 5/100))}].")

elif 12000 < valor_fabrica <= 25000:
    print(f"\nO valor do custo final do carro aplicado comissão e impostos é: "
          f"[R${(valor_fabrica + ((valor_fabrica * 10/100) + (valor_fabrica * 15/100)))}].")

elif valor_fabrica > 25000:
    print(f"\nO valor do custo final do carro aplicado comissão e impostos é: "
          f"[R${(valor_fabrica + ((valor_fabrica * 15/100) + (valor_fabrica * 20/100)))}].")

