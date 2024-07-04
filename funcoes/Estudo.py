# Estudo de return

num_01 = []

def cont(num):
    if num % 2 == 0:
        return print(f"O número digitado é par")
    else:
        return print("O número digitado é ímpar.")    

while True:
    numero = int(input("Insira um numero: "))
    num_01.append(numero)
        
    if numero % 2 == 0:
        print(cont(numero)) #Se não passar numero como argumento, a função não saberá qual número verificar
        break
    else:
        print(cont(numero)) #Se a função cont não tiver argumentos, você poderia chamá-la diretamente sem passar nenhum valor
        break