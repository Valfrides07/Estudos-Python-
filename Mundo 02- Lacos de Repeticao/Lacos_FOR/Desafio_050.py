#Um algoritmo que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares

num_int = str(input("Digite seis numeros: "))
lista_numeros = num_int.split(",")

for c in range (num_int,999, 2):
     print("Os numeros são: ", lista_numeros)