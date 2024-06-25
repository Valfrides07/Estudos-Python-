#Algoritmo que mostre o maior ou os numeros iguais entre 3 recebidos via teclado pelo usuruario

num_01 = int(input("Entre com um numero:"))
num_02 = int(input("Entre com um numero:"))
num_03 = int(input("Entre com um numero:"))


#Decisao entre quem é o maior entre eles

if num_01 > num_02 and num_03 < num_01 and num_02:
   print(f"O {num_01} é maior que o {num_02} e o {num_03}")

if num_02 > num_01 and num_03 < num_02 and num_01:
   print(f"O {num_02} é maior que o {num_01} e o {num_03}")

if num_03 > num_01 and num_02 < num_03 and num_01:
   print(f"O {num_03} é maior que o {num_01} e o {num_02}")

#Caso todos sejam iguais

elif num_01 == num_02 == num_03:
   print("Todos os numeros sao iguais!!")

#Decisao entre quais sao os iguais e quem e se tem um maior entre eles

elif num_01 == num_02:
   print(f"o {num_01} é igual ao {num_02}")

elif num_02 == num_03:
   print(f"o {num_02} é igual ao {num_03}")

elif num_03 == num_01:
   print(f"o {num_03} é igual ao {num_01}")

#Caso não sejam iguais

else: 
   print("Nenhum dos numeros inseridos são iguais!")







