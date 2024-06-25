#Refazer o desafio09 utilizando o laço for (Feito)

n = int(input("Digite um número qualquer entre 1 e 10, para ser exibido a sua tabuada: "))

for tb in range(1, 11):
    print("{} x {:2} = {}".format(n, tb, n*tb))