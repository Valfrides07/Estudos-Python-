#Um programa que leia varios valores e mostre a media entre eles, o maior e o menor deles e por fim pergunte ao usuario se ele deseja enserir novos valores ou finalizar

while True: #While True serve para que o programa entre em um Loop
    valores = []

    for nn in range (1,11):
        num =  int(input(f"Ensira o {nn}º numero: "))
        valores.append(num)#armazena os valores digitados pelo o usuario

    media = sum(valores)/len(valores) #"len(numeros)" é o número total de elementos na lista, neste contexto serve para dividir com os numeros somados
    print(f"A média dos valores digitados é: {media}")

    maior = max(valores)
    print(f"O maior valor digitado foi: {maior}")

    menor = min(valores)
    print(f"O menor valor digitado foi: {menor}") 

    decisao = str(input("Deseja enserir novos valores[sim/nao]: "))

    if decisao != "sim":
        print("Programa finalizado.")
        break #Break serve para finalizar o programa quando o usuario digitar algo diferente de "sim", caso digite "sim" o programa volta ao inicio