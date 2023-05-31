"""
50. Chico tem 1.50 metro e cresce 2 centímetro por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros por ano.
Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.
"""
print("-Chico tem 1.50 metro e cresce 2 centímetro por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros por "
      "ano.")
print("-Descubra quantos anos serão necessários para que Zé seja maior que Chico;")

altura_chico = 1.50
altura_ze = 1.10

cdg = True

nova_altura_ze = altura_ze
nova_altura_chico = altura_chico
ano = 0

while cdg:


    if nova_altura_ze > nova_altura_chico:
        print(f"\n-Será necessário {ano} anos para que Zé seja maior que Chico.")
        print(f"Em {ano} anos; Chico terá {nova_altura_chico:.2f} Metros e Zé {nova_altura_ze:.2f} Metros.")
        cdg = False

    else:
        ano = ano + 1

        nova_altura_chico = nova_altura_chico + 0.02

        nova_altura_ze = nova_altura_ze + 0.03
