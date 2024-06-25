# Um programa que leia o preço de varios produtos, o programa devera perguntar ao usuario se ele deseja continuar ou não e no final mostre a soma dos produtos,
# quantos produtos custam mais de 1.000 reais e qual é o nome do produto mais barato 
 
total = 0
mil= 0 
cont= 0

while True:
 
    produto = str(input("Informe o nome do produto: "))
    preco = float(input("O preço do produto R$:"))
    cont+= 1
    total+= preco #Este operador é uma combinação de adição (+) e atribuição (=), 
    #Ele adiciona o valor à direita do operador (preco) ao valor existente da variável à esquerda (total) e então armazena o resultado de volta na variável à esquerda (total)
        
    if preco > 1000:
        mil+= 1 #Isso é usado para contar quantos produtos têm um preço maior que 1000.
    

#cont == 1: Esta condição verifica se estamos no primeiro produto.
# preco < menor: Esta condição verifica se o preço do produto atual é menor que o preço do produto mais barato registrado até agora.
    if cont == 1 < preco:
        menor = preco
        produto_barato = produto


    perg = str(input("Deseja continuar [S ou N]: "))
    if perg == "s":
        continue
    elif perg == "n":
        break
    
    
print(f"Tem {mil} produtos custando mais de mil reais")
print(f"O menor preço é do {produto_barato} custando R$: {preco:.2f}")
print(f"E a soma total dos produtos é: {total:.3f}")