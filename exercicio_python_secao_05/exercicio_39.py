"""
39. Uma empresa decide dar um aumento aos seus funcionários de acordo com a sua tabela que considera o salário
atual e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente
maior que do que os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário
irá receber um bônus adicional de salário.
Faça um programa que leia:

* O valor do salário atual do funcionário;
* O tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final
reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

SALARIO ATUAL    | REAJUSTE(%)  | TEMPO DE SERVIÇO | Bônus     |
Até 500,00       |      25%     | Abaixo de 1 ano  | Sem bônus |
Até 1000,00      |      20%     | De 1 a 3 anos    | 100,00    |
Até 1500,00      |      15%     | De 4 a 6 anos    | 200,00    |
Até 2000,00      |      10%     | De 7 a 10 anos   | 300,00    |
Acima de 2000,00 | Sem reajuste | Mais de 10 anos  | 500,00    |
"""
print("DESCUBRA SE VAI RECEBER AUMENTO!")

print("\nSALARIO ATUAL    | REAJUSTE(%)  | TEMPO DE SERVIÇO | Bônus     |")
print("Até 500,00       |      25%     | Abaixo de 1 ano  | Sem bônus |")
print("Até 1000,00      |      20%     | De 1 a 3 anos    | 100,00    |")
print("Até 1500,00      |      15%     | De 4 a 6 anos    | 200,00    |")
print("Até 2000,00      |      10%     | De 7 a 10 anos   | 300,00    |")
print("Acima de 2000,00 | Sem reajuste | Mais de 10 anos  | 500,00    |")

salario = float(input("\nDigite o seu salário atual: "))
tempo_ano = input("Digite quantos anos de serviço você tem (Se você tem menos de um ano de serviço digite 'Não'): ")

if str(tempo_ano) == str("Não") or str(tempo_ano) == str("não"):
    tempo_meses1 = int(input(f"Digite quantos meses de servição você tem: "))
    tempo_meses2 = tempo_meses1/100
else:
    ()

if salario <= 500:
    if tempo_meses2 < 1:
        print(f"\nO seu salario é de R${salario} refente aos {tempo_meses1} meses de serviço,"
              f"teve um aumento de [R${(salario + (salario * 25/100))}]!")
    else:
        print("\n[Os dados do salário ou do tempo de serviço estão incorreto referente a tabela de reajuste!]")

elif salario <= 1000:
    if 1 <= int(tempo_ano) <= 3:
        print(f"\nO seu salario é de R${salario} refente aos {tempo_ano} anos de serviço,"
              f"teve um aumento de [R${(salario + (salario * 20 / 100)) + 100}]!")
    else:
        print("\n[Os dados do salário ou do tempo de serviço estão incorreto referente a tabela de reajuste!]")

elif salario <= 1500:
    if 4 <= int(tempo_ano) <= 6:
        print(f"\nO seu salario é de R${salario} refente aos {tempo_ano} anos de serviço,"
              f"teve um aumento de [R${(salario + (salario * 15 / 100)) + 200}]!")
    else:
        print("\n[Os dados do salário ou do tempo de serviço estão incorreto referente a tabela de reajuste!]")

elif salario <= 2000:
    if 7 <= int(tempo_ano) <= 10:
        print(f"\nO seu salario é de R${salario} refente aos {tempo_ano} anos de serviço,"
              f"teve um aumento de [R${(salario + (salario * 10 / 100)) + 300}]!")
    else:
        print("\n[Os dados do salário ou do tempo de serviço estão incorreto referente a tabela de reajuste!]")

elif salario > 2000:
    if int(tempo_ano) > 10:
        print(f"\nO seu salario é de R${salario} refente aos {tempo_ano} anos de serviço,"
              f"teve um aumento de [R${salario + 500}]!")
    else:
        print("\n[Os dados do salário ou do tempo de serviço estão incorreto referente a tabela de reajuste!]")

