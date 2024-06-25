#Crie um programa que leia varios numeros inteiros, o programa só vai parar quando o usario digitar "999" ,  no final mostre quantos numeros foram digitados    
#E a soma entre eles, desconsiderando o "999"

contador = 1
numeros = 1
valores =[]

nume = int(input(f"Digite 1º o numero: "))

while nume!= 999:
    numeros += 1
    nume = int(input(f"Digite o {numeros}º numero, lembrando que o número 999 termina o programa: "))
    valores.append(nume)  #armazena os valores digitados pelo o usuario
    contador +=1
    
    if 999 in valores: # se 999 estiver presente na lista Valores
        valores.remove(999) #remove o numero 999 da lista, assim não irá soma-lo com os demais 


    if nume == 999:
        soma = sum(valores)
        print(f"Voce digitou um total de: {contador} vezes e o total da soma desses numeros é: {soma}")  