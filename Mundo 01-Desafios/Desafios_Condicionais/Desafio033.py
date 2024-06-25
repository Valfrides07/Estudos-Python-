#Algortimo que mostra quaçl número é o maior, números recebidos via teclado pelo o usúario:

print("Informe abaixo tres numeros que deseja saber quais são os maiores entre si")

numeros_0 = int(input("Informe aqui:"))
numeros_1 = int(input("Informe aqui:"))
numeros_2 = int(input("Informe aqui:"))

#Recebe o valor de maior entre eles
maior_numero = numeros_0

if numeros_0>numeros_1 or numeros_2:
    print("O numero {} o maior numero entre eles" .format(numeros_0))

if numeros_1>numeros_2 or numeros_0:
    print("O numero {} o maior numero entre eles" .format(numeros_1))

else: numeros_2>numeros_0 or numeros_1
print("O numero {} o maior numero entre eles" .format(numeros_2))

