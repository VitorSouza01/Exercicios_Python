"""
59. Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kwh, e para cada
habitante entre com os seguintes dados: consumo do mês e o código do consumidor (1-Residencial, 2-Comercial,
3-Industrial). No final imprima o maior, o menor e a média do consumo dos habitantes;e por fim o total do consumo
de cada categoria de consumidor.
"""
cdd = input("-Digite o nome de uma cidade: ")
hbtt = int(input(f"-Digite a quantidade de habitantes em {cdd}: "))

mir_cnsm = 0
mnr_cnsm = 0
mda_cnsm = 0

ttl_cnsm_1 = 0
ttl_cnsm_2 = 0
ttl_cnsm_3 = 0

if hbtt > 0:

    # 1- R$ 0,92 kWh para tarifa residencial
    # 2 - R$ 0,86 kWh para tarifa comercial.
    # 3 - R$ 1,79 kWh para tarifa industrial.

    print("\n[ Tipo de consumidores; (1 - Residencial), (2 - Comercial), (3 - Industrial) ]")

    for n in range(1, hbtt + 1):

        tp_hbtt = int(input(f"\n-Digite o número do tipo de consumidor referente ao {n}° habitante: "))

        cnsm_kwh = int(input(f"-Digite o consumo do mês em Kwh: "))

        if tp_hbtt == 1:
            cnsm_hbtt1 = cnsm_kwh * 0.92

            if cnsm_hbtt1 > mir_cnsm:
                mir_cnsm = cnsm_hbtt1
                mda_cnsm += cnsm_hbtt1

            if cnsm_hbtt1 < mir_cnsm:
                mnr_cnsm = cnsm_hbtt1
                mda_cnsm += cnsm_hbtt1

            ttl_cnsm_1 = mir_cnsm + mnr_cnsm

        elif tp_hbtt == 2:
            cnsm_hbtt2 = cnsm_kwh * 0.86

            if cnsm_hbtt2 > mir_cnsm:
                mir_cnsm = cnsm_hbtt2
                mda_cnsm += cnsm_hbtt2

            if cnsm_hbtt2 < mir_cnsm:
                mnr_cnsm = cnsm_hbtt2
                mda_cnsm += cnsm_hbtt2

            ttl_cnsm_2 = mir_cnsm + mnr_cnsm

        elif tp_hbtt == 3:
            cnsm_hbtt3 = cnsm_kwh * 1.79

            if cnsm_hbtt3 > mir_cnsm:
                mir_cnsm = cnsm_hbtt3
                mda_cnsm += cnsm_hbtt3

            if cnsm_hbtt3 < mir_cnsm:
                mnr_cnsm = cnsm_hbtt3
                mda_cnsm += cnsm_hbtt3

            ttl_cnsm_3 = mir_cnsm + mnr_cnsm

        else:
            print("\n[O tipo de consumidor informado é inválido!]")

else:
    print("\n[A quantidade de habitantes informado é inválido!]")


print(f"\n-O maior consumo entre os habitantes de {cdd} é; [{mir_cnsm}].")
print(f"-O menor consumo entre os habitantes de {cdd} é; [{mnr_cnsm}].")
print(f"-A média do consumo dos habitantes de {cdd} é; [{mda_cnsm/2}].")

print(f"\n-O total de consumo pelos consumidores (Residencial) são; [{ttl_cnsm_1}].")
print(f"-O total de consumo pelos consumidores (Comercial) são; [{ttl_cnsm_2}].")
print(f"-O total de consumo pelos consumidores (Industrial) são; [{ttl_cnsm_3}].")
