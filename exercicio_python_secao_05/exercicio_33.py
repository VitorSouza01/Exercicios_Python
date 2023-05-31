"""
33. Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo,
e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela).

    |    PREÇO ANTIGO     | PERCENTUAL DE AUMENTO|
    | até R$ 50           |       5%             |
    | entre R$ 50 e R$ 100|      10%             |
    | acima de R$ 100     |      15%             |


    |   PREÇO NOVO                     |   MENSAGEM    |
    | até R$ 80                        |   Barato      |
    | entre R$ 80 e R$ 120 (inclusive) |   Normal      |
    | entre R$ 120 e R$ 200 (inclusive)|   Caro        |
    | acima de R$ 200                  |   Muito Caro  |

"""

print("[Descubra o Valor de Aumento!]")
preco_antigo = float(input("-Digite o valor do produto;"))

if preco_antigo <= 50:
    preco_novo = ((5/100) + 1) * preco_antigo

elif preco_antigo <= 100:
    preco_novo = ((10 / 100) + 1) * preco_antigo

elif preco_antigo > 100:
    preco_novo = ((15 / 100) + 1) * preco_antigo

if preco_novo <= 80:
    print(f"\nO valor final ficou {preco_novo}!")
    print("O produto está Barato!")

elif preco_novo <= 120:
    print(f"\nO valor final ficou {preco_novo}!")
    print("O produto está Normal!")

elif preco_novo <= 200:
    print(f"\nO valor final ficou {preco_novo}!")
    print("O produto está Caro!")

elif preco_novo > 200:
    print(f"\nO valor final ficou {preco_novo}!")
    print("O produto está Muito Caro!")







