#Algoritmo que informa qual é o ano bissexto
ano = int(input("Informe qual ano voce deseja saber se é bissexto ou não é: "))

#conta a ser feita para informar se é ou não um ano bissexto
ano_bissexto = ano % 4

#caso for um ano bissexto será informado, caso contrário tambem será informado.
if ano_bissexto == 0:
    print("O ano de {} é um ano bissexto, contendo 366 dias em seu calendário." .format(ano))

else:
    print("Não é um ano bissexto.")