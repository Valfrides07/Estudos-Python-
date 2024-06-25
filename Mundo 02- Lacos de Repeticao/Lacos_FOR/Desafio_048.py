#Um Algoritmo que calcule a soma dos numeros impares que são multiplos de tres entre 1 e 500

#não vai ate 500, sendo que esta indo de 3 e 3(por serem Impáres), entao 500/3 = 166 numeros apresentados
for np in range(0 , 500, 3 ):

#indo de 3 em 3, então crio um laço que vá ate 166 de 1 em 1 para que sejam os seus multiplicadores (3x1, 6x2) e assim por diante. 
    for im in range(0, 166, 1):
          #Esse laço "im" gera numeros de 1 em 1, então ele dever ser multiplicado com o laço for "np" que os números são gerados de 3 em 3.
          calculo = np * im
    print(np)
print("Fim")