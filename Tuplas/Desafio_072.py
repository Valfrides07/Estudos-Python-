# Um programa que leia um numero digitado pelo usuario entre 0 e 20 e mostre ele por extenso(10 = dez), utilizando tuplas

nums = ("Zero", "Um", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quartoze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte") # Tuplas de números por extenso 

while True:

    numeracao = int(input("Digite um numero entre 0 e 20: "))
    if 0 <=  numeracao >=20:
        continue
    print(f"O número {numeracao} é {nums[numeracao]} por extenso.") #{nums[numeracao]} deve conter a índice dentro dos colchetes para que possa ser acessado as informações
    break