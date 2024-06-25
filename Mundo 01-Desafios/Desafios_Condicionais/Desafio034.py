#Receber via teclado o salário menor ou igual a 1.250(recebe um aumento de 15%) se maior que 1250(aumento de 10%)
salario_receba = float(input("caro colaborador inmforme o seu salario para que seja calculado o aumento:"))

#contas a serem feitas para difernciar se recebe aumento de 10% ou 15%
aumento_de_10 = salario_receba * 0.10
aumento_de_15 = salario_receba * 0.15

#mostra qual o novo salário, junto com a porcentagem, em cima do salario base 
if salario_receba<=1250:
    novo_salario15 = aumento_de_15 + salario_receba
    print("O seu novo salário sera de {}!" .format(novo_salario15))

if salario_receba>=1251:
    novo_salario10 = aumento_de_10 + salario_receba
    print("O seu novo salario será de {}, aproveite" .format(novo_salario10))
 
