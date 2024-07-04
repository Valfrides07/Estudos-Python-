# Um programa que leia varios numero e que armazene cada numero em uma lista geral com todos esses numeros, uma somente com numeros pares e outra somente com numeros impares

lista_Geral = []
lista_Par = []
lista_Impar = []

while True:
    nums = int(input("Ensira o numero que deseja: "))
    lista_Geral.append(nums)
    
    if nums % 2 == 0: # Se o numero digitado pelo o usuario foi divido por 2 e resultar em 0, é adicionado a lista par
        lista_Par.append(nums)
    
    else: # Caso nao seja adicionado a lista par, ele é impar e então adicionado a lista impar
        lista_Impar.append(nums) 
    
    nums_1 = input("Deseja enserir um novo numero? ")
    
    if nums_1 == "sim" or nums_1== "s":
        continue
        
    elif nums_1 == "nao" or nums_1== "n":
        print(f"Os numeros adicionados são: {lista_Geral}")
         
    
    print(f"Os numeros Pares adicionados são: {lista_Par}")
    print(f"Os numeros Impares adicionados são: {lista_Impar}")
    break
    