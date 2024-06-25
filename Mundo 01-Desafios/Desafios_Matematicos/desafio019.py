#Importando o módulo
import random

#1-variaveis, entre colchetes dessa forma para serem usadas, colchetes sao utilizados quando pode haver mudanças nas variaveis, diferentes de parenteses que sao usados q
#2-quando há ideia de mudancas
nomes = ['julia', 'thiago', 'marcos', 'alice']

nome_aleatorio = random.choice(nomes)

print("o nome escolhido para apagar a lousa é: {}." .format(nome_aleatorio))