dias = int(input("Por favor informe quantos dias voce ira alugar o carro, lembrando que custa 60 reais:"))

aluguel = dias * 60

distancia = float(input("Agora diga quantos quilometros foram percorridos:"))

km = distancia * 0.15

total = aluguel + km

print(f"O valor sobre o aluguel do veiculo é: {aluguel:.2f}, e de acordo com a distancia percorrida voce deve pagar: {km:.2f} reais, totalizando: {total:.2f}")