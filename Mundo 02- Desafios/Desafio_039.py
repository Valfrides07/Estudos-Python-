#Algoritmo que informe quando um jovem deverá se apresentar ou se já passou da data de apresentação no EB

#Algoritmo que leia a data de nascimento desse jovem e informe se ele ainda devera se apresentar, se ja esta no momento de se apresentar ou então se ja apssou da hora de se apresentar

nome_usuario = str(input("Insira o seu nome conscrito: "))
idade_usuario = float(input("Insira o ano de seu nascimento:"))

avaliacao_de_idade = 2024 - idade_usuario 

#Se o usuario tiver 17 anos, deverá se alistar, menos deverá aguardar até o proximo ou os proximos anos e se tiver mais de 17 anos deverá se apresentar

if avaliacao_de_idade == 17:
    print(f"{nome_usuario}, Voce devera se alistar no site do Exército Brasileiro e aguardar as próximas etapas, acompanhando o seu e-mail.")

elif avaliacao_de_idade < 16:
    print(f"{nome_usuario}, Voce ainda não esta no ano de alistamento, aguarde.")

else: 
    print(f"{nome_usuario}, Voce já passou do ano de alistamento, compareça o quanto antes no quartel mais próximo de sua residencia para justificar a sua falta de compromisso.")