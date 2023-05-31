"""
45. Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa.
Você deve criar um menu com as duas opções de conversão e com uma opção para finalizar o programa.
O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado quando
a opção de finalizar for escolhida.

1 metro = 0,001 Quilometro
1 Quilometro = 1000
"""
cdg = True

while cdg:

	print("[--------------------------]")
	print("[ CONVERSOR DE KM/H E M/S  ]")
	print("[--------------------------]")
	print("[OPÇÕES;                   ]")
	print("[OPÇÃO 1; DE KM/H PARA M/S.]")
	print("[OPÇÃO 2; DE M/S PARA KM/H.]")
	print("[OPÇÃO 3; ENCERRAR PROGRAMA]")
	print("[--------------------------]")

	opc0 = int(input("\n-Digite uma das opções; "))

	if opc0 > 0:
		if opc0 == 1:
			km = float (input("\n-Digite o valor de Km/h; "))
			cnvs = km * 1000
			print(f"\n[A CONVERSÃO DE {km} KM/H PARA M/S É;]")
			print(f"[{cnvs} M/S]\n")

		elif opc0 == 2:
			ms = float(input("\n- Digite o valor de M/s; "))
			cnvs = ms * 0.001
			print(f"\n[A CONVERSÃO DE {ms} M/S PARA KM/S É;]")
			print(f"[{cnvs} KM/H]\n")

		elif opc0 == 3:
			cdg = False
			print("\n[O PROGRAMA FOI ENCERRADO! ]")

		else:
			print("\n[      OPÇÃO INVALIDA!     ]\n")

	else:
		print("\n[      OPÇÃO INVALIDA!     ]\n")
