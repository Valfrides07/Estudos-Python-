#Algortimo que calcule o imc da uma pessoa, o calculo deve ser feito da seguinte forma:

#Fazer o cálculo do IMC é bem fácil. Primeiro, você vai multiplicar o valor de sua altura (em metros) por ele mesmo. Por exemplo, se você medir 1,60 metros, o cálculo será:
#1,6 x 1,6 = 2,56
#Em seguida, deverá ser dividido pelo valor obtido acima. Pensando no mesmo exemplo anterior, se o seu peso for 60 quilos, a conta será:
#60 ÷ 2,56 = 23,43

altura = float(input("Insira a sua altura em metros: "))
peso = float(input("Insira o seu peso: "))

#Calculo de IMC

multi_altura = altura * altura
div_altu_peso = peso / multi_altura

#Decisões de abaixo do peso(abaixo de 18.5), peso ideal(18.5 a 25), sobrepeso(25 a 30), obesidade(30 a 40) e obesidade Mórbida(acima de 40)

if div_altu_peso < 18.5:
    print(f"Voce possui um IMC considerado Abaixo do peso de: {div_altu_peso:.1f}")
#

if div_altu_peso > 18.6:
    print(f"Voce possui um IMC considerado Ideal de: {div_altu_peso:.1f}")

if div_altu_peso < 25:
    print(f"Voce possui um IMC considerado Ideal de: {div_altu_peso:.1f}")
#

elif div_altu_peso > 25.1:
    print(f"Voce possui um IMC considerado peso Sobrepeso de: {div_altu_peso:.1f}")

elif div_altu_peso < 30:
    print(f"Voce possui um IMC considerado peso Sobrepeso de: {div_altu_peso:.1f}")    
#

elif div_altu_peso > 30.1:
     print(f"Voce possui um IMC considerado Obesidade de: {div_altu_peso:.1f}")

elif div_altu_peso < 40:
     print(f"Voce possui um IMC considerado Obesidade de: {div_altu_peso:.1f}")     
#

else:
     print(f"Voce possui um IMC considerado Obesidade Mórbida de: {div_altu_peso:.1f}")