salario = float(input("Por favor colaborador, informe o seu salario para que seja calculado o novo proporcional a sua promoção:"))

aumento_salarial = salario+(salario * 0.15)

print(f"Parabéns pelo seu auemento, esse é o seu novo salario:{aumento_salarial:.2f}".format(aumento_salarial))