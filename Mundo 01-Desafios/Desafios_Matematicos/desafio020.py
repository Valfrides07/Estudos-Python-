#Importando o módulo
import random

#1-variaveis, entre colchetes dessa forma para serem usadas, colchetes sao utilizados quando pode haver mudanças nas variaveis, diferentes de parenteses que sao usados q
#2-quando há ideia de mudancas
nomes = ['Flavia', 'Rodrigo', 'marcos', 'alice', 'Claudio', 'Fabio', 'Renata', 'Larissa', 'Isabella']

nome_aleatorio = random.choice(nomes)

print("o nome escolhido para apresentar o trabalho é: {}." .format(nome_aleatorio))