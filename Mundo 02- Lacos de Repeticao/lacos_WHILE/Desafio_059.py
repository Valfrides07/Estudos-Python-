#Um Programa que leia dois valores e mostre um menu na tela 1[SOMAR], 2[MULTIPLICAR], 3[MAIOR], 4[NOVOS NUMEROS], 5[SAIR DO PROGRAMA]  
#o programa deverá realizar a operação solicitada em cada caso

while True:
    valores = []

    for v in range (1,3):
        valor = int(input(f"Ensira o {v}º valor: "))
        valores.append(valor)  # Adiciona o valor na lista

    # " \n " serve para quebrar linhas
    escolhas_1 = int(input("[1] SOMAR \n[2] MULTIPLICAR \n[3] QUAL O MAIOR NÚMERO \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA \n ESOLHA UMA DAS OPÇÕES: "))

    while escolhas_1 == [1,2,3,4,5]:
        escolhas_1 = int(input("[1] SOMAR \n[2] MULTIPLICAR \n[3] QUAL O MAIOR NÚMERO \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA \n ESOLHA UMA DAS OPÇÕES: "))

    if escolhas_1 == 1:
        soma = valores[0] + valores[1]
        print(f"A soma dos valores: {valores[0]} e {valores[1]}, digitados são {soma}")

    elif escolhas_1 == 2:
        multiplicacao = valores[0] * valores[1]
        print(f"A multiplicação dos dois: {valores[0]} e {valores[1]}, é: {multiplicacao}")
    
    elif escolhas_1 == 3:
        maior = max(valores)
        print(f"O maior valor digitado foi: {maior}.")

    if escolhas_1 == 4:
        continue  #Continue serve para retornar a proxima Iteração (proximo dado que o usuario pode entrar dentro do Loop)

    elif escolhas_1 == 5:
        valores.clear() #Serve para limpar as variaveis ja armazenadas
        print("Programa Finalizado.")
        break   #Se o usuario digitar "5" o programa irá finalizar

    else:
        print("Digite um valor Válido.")
        continue #Continue serve para retornar a proxima Iteração (proximo dado que o usuario pode entrar dentro do Loop)
