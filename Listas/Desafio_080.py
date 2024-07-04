# Crie um programa onde o usuario possa digitar 5 valores numericos e cadraste-os em uma lista ja na poisção correta sem utilizar sort() no final mostre a lista ordenada

while True:

    list = []

    for l in range(1,6):
        numeros = int(input("Ensira o numero que deseja: "))
        list.append(numeros)

        
        if numeros < 0 or numeros > 999:
            print("Ensira um numero que seja válido.")
            continue
# REVISAR!!