#Vindo da Biclioteca Random e importando o modulo Randint
from random import randint
n = int(input("Olá usuario, tente acertar o número que estou pensando entre 0 e 5: "))

#sera gerado um numero aleatorio pela maquina entre 0 e 5
computador = randint(0,5)

# Se o numero digitado na varial N for o mesmo gerado pela maquina na Variavel COMPUTADOR, sera verdadeiro(If)
if n == computador:

    print("Foi esse número que pensei!!")

#Caso contrário, sera Falso(Else)
else: 
     
    print("HAHA voce errou, pensei em outro numero")