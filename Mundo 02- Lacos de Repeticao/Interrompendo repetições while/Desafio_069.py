#Um programa que leia a idade e sexo de varias pessoas. A cada pessoa cadastrada o programa devera perguntar se o usuario quer ou nao continuar. 
# Ao final mostre: Quantas pessoas tem mais de 18 anos, Quantos homens foram cadastrados e quantas mulheres com menos de 20 anos foram cadastradas

while True:
    pess_18 = []
    homens = []
    mul_20 = []

    idade = int(input("Informe a sua idade: "))

    if idade < 1:
        print("Insira uma idade válida!")
        continue 
    if idade > 110:
        print("Insira uma idade válida!")
        continue 

    sx = input("Informe o seu genero M ou F: ")

    if sx != "m" and "f":
        print("Um genero válido.")
        continue

    cont = input("Desejar continuar? ")
    
    if cont == "sim":
        continue #Irá enserir os dados novamente

    elif cont == "nao":
        if idade > 18:
            pess_18.append(idade)
            break # Encerra o programa e mostra os dados enseridos pelo usuario
    
    if cont != "sim" or "nao":
        print("Por favor, responda somente com sim ou nao.")
        continue

    if sx == "m":
        homens.append(sx) # Armazena os dados enseridos pelo usuario na variavel SEXX dentro da array HOMENS 
    
    if idade < 20:
        if sx == "f":
            mul_20.append(idade)

# LEN serve para mostrar a quantidades de dados enseridos, se o usuario digitou 5 vezes a idade, irá mostrar a quantidade de vezes e não a idade
print(f"A quantidade de pessoas com mais de 18 anos é: {len(pess_18)}")
print(f"A quantidade de homens cadastrados é: {len(homens)}")
print(f"A quantidade de mulheres com menos de 20 anos é: {len(sx)}")


