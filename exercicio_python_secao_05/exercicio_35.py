"""
35. Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o
dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
"""
print("[ DESCUBRA SE A DATA É VÁLIDA ]")
print("\nObs:A data tem que preencher  todos os campos igual o exemplo: 01/01/2021")
data = str(input("-Digite aqui a data;"))

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

if (ano % 4) == 0:
    # É ano bissexto.
    if mes == 1:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 2:
        if 0 < dia <= 29:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 3:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 4:
        if 0 < dia <= 30:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 5:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 6:
        if 0 < dia <= 30:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 7:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 8:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 9:
        if 0 < dia <= 30:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 10:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 11:
        if 0 < dia <= 30:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 12:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")


else:
    # Não é ano bissexto.
    if mes == 1:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 2:
        if 0 < dia <= 29:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 3:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 4:
        if 0 < dia <= 30:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 5:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 6:
        if 0 < dia <= 30:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 7:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 8:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 9:
        if 0 < dia <= 30:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 10:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 11:
        if 0 < dia <= 30:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")

    elif mes == 12:
        if 0 < dia <= 31:
            print(f"\n[A data {data} é Válida!]")
        else:
            print(f"\n[A data {data} NÃO é Válida!]")
