"""
32. Escreva um programa que leia o código do produto escolhido do cardápio de uma
lanchonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que cada execução somente será calculado um pedido.
O cardápio da lanchonete segue o padrão abaixo;

|ESPECIFICAÇÃO   |  CÓDIGO  |   PREÇO   |
|Cachorro Quente |   100    |   1.20    |
|Bauru Simples   |   101    |   1.30    |
|Bauru com Ovo   |   102    |   1.50    |
|Hamburguer      |   103    |   1.20    |
|Cheeseburguer   |   104    |   1.70    |
|Suco            |   105    |   2.20    |
|Refrigerante    |   106    |   1.00    |
"""

print("-- FAÇA O SEU PEDIDO DA LANCHONETE! -- ")
print("Obs: Limite de pedido por vez 1.")

print("\n┌───────────────────────────────────────┐")
print("|                 CARDÁPIO              |")
print("|ESPECIFICAÇÃO   |  CÓDIGO  |   PREÇO   |")
print("|Cachorro Quente |   100    |   1.20    |")
print("|Bauru Simples   |   101    |   1.30    |")
print("|Bauru com Ovo   |   102    |   1.50    |")
print("|Hamburguer      |   103    |   1.20    |")
print("|Cheeseburguer   |   104    |   1.70    |")
print("|Suco            |   105    |   2.20    |")
print("|Refrigerante    |   106    |   1.00    |")
print("└───────────────────────────────────────┘")

codigo = int(input("\nDigite o código do seu pedido:"))
quantidade = int(input("Digite a quantidade do pedido escolhido:"))

if codigo == 100:
    print(f'\n- Você escolheu {quantidade} Cachorro Quente!')
    print(f'- O Valor final no total fica: [R${1.20*quantidade}]')
elif codigo == 101:
    print(f'\n- Você escolheu {quantidade} Bauru Simples!')
    print(f'- O Valor final no total fica: [R${1.30 * quantidade}]')
elif codigo == 102:
    print(f'\n- Você escolheu {quantidade} Bauru com Ovo!')
    print(f'- O Valor final no total fica: [R${1.50 * quantidade}]')
elif codigo == 103:
    print(f'\n- Você escolheu {quantidade} Hamburguer!')
    print(f'- O Valor final no total fica: [R${1.20 * quantidade}]')
elif codigo == 104:
    print(f'\n- Você escolheu {quantidade} Cheeseburguer!')
    print(f'- O Valor final no total fica: [R${1.70 * quantidade}]')
elif codigo == 105:
    print(f'\n- Você escolheu {quantidade} Suco!')
    print(f'- O Valor final no total fica: [R${2.20 * quantidade}]')
elif codigo == 105:
    print(f'\n- Você escolheu {quantidade} Refrigerante!')
    print(f'- O Valor final no total fica: [R${1.00 * quantidade}]')
else:
    print('\n- Erro! Código inválido!')







