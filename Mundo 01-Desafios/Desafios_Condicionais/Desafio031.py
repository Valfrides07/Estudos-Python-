#Algoritmo que consulta quanto o passageiro irá pagar por Km
quantidade_de_km = float(input("Insira quantos km de viagem será: "))

#abaixo de 200km pagará 0.50 centavos por km percorrido 
if quantidade_de_km <=200:
    valor_pago = quantidade_de_km * 0.50
    print(f"O valor a ser pago é de: {valor_pago:.2f} Reais" .format(valor_pago))

#acima de 201KM pagará 0.45 centavos por Km percorrido
else:

    valor_maior = quantidade_de_km * 0.45
    print(f"O valor a ser pago é de: {valor_maior:.2f} Reais" .format(valor_maior))