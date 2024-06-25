
#alterar codigo com base o Desafio042

#Algortimo para mostar se é possivel montar um triangulo
a = float(input("Informe a RETA numero 1: "))
b = float(input("Informe a RETA numero 2: "))
c = float(input("Informe a RETA numero 3: "))

#Conta a ser realizada para saber se é possivel montar um algoritmo
lado_1 = a + b > c
lado_2 = c + a > b

if lado_1 > lado_2 or lado_2 > lado_1:
    print("É possivel montar um triangulo")

else:
    print("Não é possivel montar um trinagulo")