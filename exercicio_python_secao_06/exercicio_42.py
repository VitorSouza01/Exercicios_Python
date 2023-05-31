""""
42. Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e
escreva para cada um dos valores lidos, o quadrado, o cubo, e a raiz quadrada.
Finalize a entrada de dados com um valor negativo ou zero.
"""
print("[Descubra o quadrado, o cubo e a raiz quadrado de um número!]")
print("Obs; Ao digitar zero ou um número negativo o código é finalizado")

cdg = True

while cdg:
    pgt = str(input("\n-Você deseja executar o código?[Sim/Não] "))

    if pgt == "Sim" or pgt == "sim":
        nmr = float(input("\n-Digite o valor de um número: "))
        if nmr > 0:
            qdd = nmr*nmr
            cb = nmr*nmr*nmr
            rqdd = nmr ** (1/2)

            print("\nO valor ao Quadrado de {:.1f} é; {:.2f}".format(nmr, qdd))
            print("O valor ao Cubo de {:.1f} é; {:.2f}".format(nmr, cb))
            print("O valor da Raiz Quadrada de {:.1f} é; {:.2f}".format(nmr, rqdd))

        elif nmr <= 0:
            cdg = False
            print("\nO Código Foi Finalizado!")

    elif pgt == "Não" or pgt == "Nao" or pgt == "não" or pgt == "nao":
        cdg = False
        print("\nO Código Foi Finalizado!")

    else:
        print("\n* Não entendi o que você quis dizer! Tente novamente!")
