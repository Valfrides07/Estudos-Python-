# Crie um programa que vai gerar 5 numeros aleatorios e colocar dentro de uma tupla e após isso mostre a listagem de numeros e tambem mostre o menor e o maior valor dentro da tupla 

import random

lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sublista = lista[2:]

# Gera uma amostra de 5 números aleatórios da sublista
numeros_aleatorios = random.sample(sublista, 5) #Usando essa sublista com a função random.sample, você terá mais variação nos números selecionados aleatoriamente, porque a sublista contém mais elementos do que a original [6, 7, 8, 9, 10].
print(numeros_aleatorios)

maior = max(numeros_aleatorios)
print(f"O maior numero apresentado foi o: {maior}")

menor = min(numeros_aleatorios)
print(f"O menor numero apresentado foi o: {menor}")
