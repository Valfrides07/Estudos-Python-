#Faça um programa que leia o sexo de uma pessoa mas só aceite M ou F, caso digite errado peça a digitação novamente ate que esteja correta

genero = str(input("Diga o seu Genero [F ou M]: "))

while genero != "F" and "M":    #Enquanto sexo não for igual a "F" ou "M" irá repetir até se tornar real 
    genero = input("Digite novamente, somente com [F ou M]: ")

if genero == "F" and "M":   #Se for real, irá finalizar
    print("Acabou")