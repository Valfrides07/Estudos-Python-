#Um algoritmo que leia o ano de nascimento do usuario, e informe quais faixas etarias ele se encaixa, mirim, infantil, junior, senior ou master

idade_do_usuario = float(input("Entre com o ano de seu nascimento por favor:"))

calculo_idade = 2024 - idade_do_usuario

if calculo_idade < 9:
    print("Voce se encaixa na faixa etaria Mirím")

elif calculo_idade < 14:
    print("Voce se encaixa na faixa etaria Junior")

elif calculo_idade < 20:
    print("Voce se encaixa na faixa etaria Senior")

else:
    print("Voce se encaixa na faixa etaria Master")