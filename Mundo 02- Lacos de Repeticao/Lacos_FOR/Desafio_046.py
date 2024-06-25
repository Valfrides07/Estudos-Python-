#Um algoritmo que mostre na tela uma contagem regressiva para o estouro de fogos de artíficio indo de 10 até 0, com uma pausa de 1 seg entre eles
#Usar a biblioteca para a contagem 

from time import sleep

for fgs in range (10 ,-1, -1):
    print (fgs)
    sleep(1.3)
print("BUMMM BUUM BUM")