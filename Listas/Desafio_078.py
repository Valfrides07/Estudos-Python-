# Um programa que leia 5 valores, mostre o menor e o maior e em qual posição estão

valores= []

for n in range(1,6):
    numero = int(input(f"Ensira o {n}º valor: "))
    valores.append(numero) #armazena os valores digitados pelo o usuario

# Encontrar o menor e maior valor digitado e mostrar a posição e quais são eles
maior = max(valores)
poiscao_maior = valores.index(maior) 

menor = min(valores)
posicao_menor = valores.index(menor) #Variavel.index(menor_valor) retorna o índice da primeira ocorrência(menor é a ocorrencia) de menor_valor na lista


print(f"O maior valor é: {maior} e a posição dele é: {poiscao_maior}")
print(f"O menor valor é: {menor} e a posição dele é: {posicao_menor}")


