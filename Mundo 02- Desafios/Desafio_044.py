#Um Algoritmo que calcule o valor a ser pago pelo cliente considerando a condição de pagamento
#A vista(dinheiro/Pix: 10% de desconto), A vista(Cartão: 5% de desconto), Em até 2x no cartão: Preço normal, 3x ou mais: 20% de juros

valor_produto = float(input("Entre com o valor do produto: "))

#Decisao de pagamento parcelado ou a vista
decisao1 = print(" (1) Dinheiro/Pix")
decisao2 = print(" (2) A Vista cartão")
decisao3 = print(" (3) Em até 2 vezes")
decisao4 = print(" (4) Em 3 vezes ou mais")

forma_de_pagamento = str(input("Infome a forma de pagamento escolhida: "))

if forma_de_pagamento == "1":
     desconto = valor_produto * 0.10
     valor_final = valor_produto - desconto
     print(f"O valor já com o desconto de 10% aplicado é: {valor_final:.2f} Reais")

#Revisar essa conta de porcentagem, pois está errada!
if forma_de_pagamento == "2":
     desconto_cartao = (5/100) * valor_produto
     print(f"O valor com o desconto de 5% aplicado é: {desconto_cartao:.2f} Reais")

#em ate 2x no cartao
elif forma_de_pagamento == "3":
     print(f"O valor do produto é de: {valor_produto:.2f}")

#em 3x ou mais com juros de 20%
elif forma_de_pagamento == "4":
     parcelas = int(input("Em quantas vezes deseja parcelar? "))
     juros_de_20 = valor_produto * 1.20
     valor_parcelas = juros_de_20/parcelas
     qnt_parcelas = print(f"São: {parcelas} parcelas, de: {valor_parcelas:.2f} Reais")
    #  juros_de_20 = valor_produto * 1.20
    #  print(f"O valor do produto com o juros aplicado é de: {juros_de_20:.2f}")

#Caso na decisão de forma de pagamento seja inserido dados não correspondentes
else:
    print("Comando inválido.")
     