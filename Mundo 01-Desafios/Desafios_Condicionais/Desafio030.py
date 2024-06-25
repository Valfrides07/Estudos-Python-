#Algoritmo que mostra se o numero recebido via teclado pelo usário é IMPAR ou PAR
import random
par_impar = int(input("Digite um numero, para que possa ser mostrado se é PAR  ou ÍMPAR: "))

#Conta que será utilizada
consulta = par_impar % 2 

if consulta == 0:
    print("O número é Par")

else:
    print("O número é Impar")
