#entrando com os dados via teclado para o calculo da hipotenusa
cateto1 = int(input("Digite o lado c2 da hipostenusa: "))
cateto2 = int(input("Digite o lado c3 da hipostenusa: "))

#Calculo dos lados do cateto para resultar a hiopotenusa 
hipotenusa = (cateto1**2 + cateto2**2)**0.5

#Resultados dos lados dos catetos e resultado da hipotenusa
print(f"Os lados da hipotenusa são: {hipotenusa:.2f} ")