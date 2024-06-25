#algoritmo que mostre uma mensagem multando um motorista caso ultrapasse o limite da via de 80km.
limite_de_velocidade = int(input("Caro Guarda de transito por favor informe qual limte da via que o veículo estava dirigindo: "))

#a multa é aplicada caso o motorista esteja acima do limite da via
if limite_de_velocidade >=81:

#subtração em cima do valor a mais do limte da via(80km), para que o km a mais seja levado em considereção
    subtracao = limite_de_velocidade - 80
    valor_multa = subtracao * 7
#valor da multa que deve ser aplicada sobre o motorista
    print(f"O motorista estava acima do limite da via, então o valor de multa a ser pago é de: {valor_multa:.2f} Reais" .format(valor_multa))

#caso ele esteja abaixo do limite de velocidade da via
else:
    print("O motorista estava dentro do limite de velocidade, não há valor de multa a ser pago.")