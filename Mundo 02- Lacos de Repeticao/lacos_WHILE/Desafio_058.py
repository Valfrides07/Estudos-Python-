#Melhorar o DESAFIO028, agora invés de ir de 0 a 10, o jogador irá advinhar até acertar mostrando quantos palpites foram necessários ate vencer 

from random import randint   # Uma biblioteca que importa números aleatórios
contador = 1

n = int(input("Olá usuario, tente acertar o número que estou pensando entre 0 e 10: "))

computador = randint(0,10)  #sera gerado um numero aleatorio pela maquina entre 0 e 5

while n != computador:  #Enquanto "n" for diferente de "computador" ira solicitar que o usario repita
    n = int(input("HAHA voce errou, pensei em outro numero: "))
    contador += 1

if n == computador:  # Se o numero digitado na variavel N for o mesmo gerado pela maquina na Variavel COMPUTADOR, sera verdadeiro(If)
    print(f"Parábens, voce acertou com um numero de {contador} tentativas!")
