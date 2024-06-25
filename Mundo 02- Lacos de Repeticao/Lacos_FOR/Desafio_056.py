#Um Algortimo que leia idade,sexo e nome de 4 pessoas. E no final mostre a média de idade do grupo, qual é o nome do homem mais velho 
#E quantas mulheres tem menos de 20 anos 



for i in range(4):
    nome = str(input(F"Diga o {i+1}º nome: "))
    idade = int(input(f"Ensira a {i+1}º idade: "))
    sexo = str(input("Ensira o Genero que se indentifica sendo, Hétero-Homem(H) Hétero-Feminino(M) Transsexual(T): "))
    calculo_idade = idade/4

    if sexo == "H" or "h" :
        print(f"A méida de idade do grupo é de {calculo_idade:.2f} anos,")
    

    # if sexo == "H" or "h":
    #     confrimacao = str(input(f"O nome digitado foi {nome}, a idade {idade} e o sexo Hétero-Homem, correto? "))

    # elif sexo == "M" or "m":
    #     confrimacao2 = str(input(f"O nome digitado foi {nome}, a idade {idade} e o sexo Hétero-Feminino, correto? "))

    # elif sexo == "T" or "t":
    #     confirmacao3 = str(input(f"O nome digitado foi {nome}, a idade {idade} e o sexo Transsexual, correto? "))

    #     calculo_idade = idade/4

    

