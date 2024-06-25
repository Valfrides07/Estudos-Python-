print("Por favor informe a largura e altura da parede para que possa ser feito o calculo")

altura = float(input("Informe a altura:"))
largura = float(input("informe a largura:"))

area = altura * largura

quantidade_tinta = area/2

print(f"a Area da parede é:{area:.2f}M".format(area))
print(f"a quantidade necessaria de tinta é:{quantidade_tinta:.2f}L".format(quantidade_tinta))