"""
38. Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mês e Ano.
Teste a validade desta data para saber se esta é uma data válida.
Teste se o dia fornecido é um dia válido: dia > 0, dia < 28 para o mês de fevereiro (29 se ano for bissexto),
dia < 30 em abril, junho, setembro e novembro, dia < 31 nos outros meses.
Teste a validade do ano: ano < ano atual (use uma constante definada com o valor igual a 2008).
Imprimir: "data válida" ou "data inválida" no final da execução do programa.
"""
print("Digite a sua data de nascimento!" "\nExemplo; ( dd mm aaaa ).")
dia, mes, ano = [int(x) for x in input("Digite aqui: ").split()]

ano_atual = 2008

if ano < ano_atual:
    if mes == 1:
        if 0 < dia < 32:
            print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
        else:
            print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    elif mes == 2:
        if (ano % 400 == 0) or (ano % 4 == 0) is not (ano % 100 == 0):
            if 0 < dia < 30:
                print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
            else:
                print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")
        else:
            if 0 < dia < 29:
                print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
            else:
                print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    elif mes == 3:
        if 0 < dia < 32:
            print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
        else:
            print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    elif mes == 4:
        if 0 < dia < 31:
            print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
        else:
            print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    elif mes == 5:
        if 0 < dia < 32:
            print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
        else:
            print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    elif mes == 6:
        if 0 < dia < 31:
            print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
        else:
            print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    elif mes == 7:
        if 0 < dia < 32:
            print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
        else:
            print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    elif mes == 8:
        if 0 < dia < 32:
            print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
        else:
            print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    elif mes == 9:
        if 0 < dia < 31:
            print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
        else:
            print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    elif mes == 10:
        if 0 < dia < 32:
            print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
        else:
            print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    elif mes == 11:
        if 0 < dia < 31:
            print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
        else:
            print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    elif mes == 12:
        if 0 < dia < 32:
            print(f"\nA data {dia}/{mes}/{ano} é [Válida]!")
        else:
            print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")

    else:
        print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")
else:
    print(f"\nA data {dia}/{mes}/{ano} é [Inválida]!")
