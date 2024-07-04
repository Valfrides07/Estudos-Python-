#Desenvolver um programa que leia quatro valores e guarde-os em uma tupla e no final, mostre: Quantas vezes apareceu o valor 9, Em qual posição foi digitado o valor 3 e Quais foram os numeros Pares.

lista=[]
cont = 0

for n in range(1,5):
    valor = input(f"Digite o {n}º valor: ")

    # Converter o valor para o tipo desejado, por exemplo, inteiro
    valor = int(valor)
    lista.append(valor)

    # Converte a lista de valores para uma tupla
    minha_tupla = tuple(lista)  
    
    # Faz uma verificação se há a existencia do numero 9 
    if valor == 9:
        cont +=1
    
print(f"Os numeros são: {minha_tupla}")

posicoes_3 = [pos for pos, val in enumerate(minha_tupla) if val == 3]

# Verifica se foram encontradas posições e exibe o resultado
if posicoes_3:
    print(f"O número 3 está nas posições: {posicoes_3}")
else:
    print("O número 3 não foi digitado.")

print(f"O valor 9 apareceu {cont} vezes.")

