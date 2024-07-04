# Um programa que vai ler varios numeros e coloca-los dentro de uma lista, mostrar quantos numeros foram digtados, a lista desses numeros de forma decrescente e se o valor 5 foi digitado e esta ou não na lista.

numeros= []

while True:
    num = int(input("Ensira o numero que deseja: "))
    numeros.append(num)
    
    pgt =input("Deseja enserir um novo numero? ")
    
    numeros.sort(reverse=True)

    if pgt == "sim" or pgt == "s":
        continue
    elif pgt == "nao" or pgt== "n":
        if 5 in numeros:
            print(f"A quantidade de numeros enseridos foram: {len(numeros)}, esses numeros de forma decrescente é: {numeros} e há a existencia do numero 5.")
            break
        else:
            print(f"A quantidade de numeros enseridos foram: {len(numeros)}, esses numeros de forma decrescente é: {numeros} e não há a existencia do numero 5.")
            break
    else:
        print("Insira uma resposta válida (sim ou não).")
        continue
