#Algortimo para mostar se é possivel montar um triangulo - O MESMO EXERCICIO QUE O 035
a = float(input("Informe a RETA numero 1: "))
b = float(input("Informe a RETA numero 2: "))
c = float(input("Informe a RETA numero 3: "))

#Decisao se é possivel montar um triangulo

if a + b > c or a + c > b:
    print("É possivel montar um triangulo")

#analise se os lados sao iguais

elif a == b or b == c:
    print(" Dois lados são iguais")
     
#todos lados iguais

elif a == b == c:
    print("Todos os lados são iguais")

else:
    print("Não é possivel montar um trinagulo")