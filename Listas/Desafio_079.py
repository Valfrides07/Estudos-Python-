# Um programa para que o usuario possa digitar varios números, cadastre cada um deles em uma lista caso o numero digitado ja tenha sido adicionado, ele nao sera adicionado novamente e no final sera mostrado todos o valores digitadis em ordem númerica

num = [] 

while True:
    numero = int(input("Digite um numero: "))
    
    if numero in num:  # Verifica se o número digitado já está na lista e retorna para a solicitação
        print("Número já enserido, digite um válido.")
        continue

    num.append(numero) # num.append(numero) adiciona o número fornecido à lista num.

    pg_s_n = input("Deseja adicionar mais um?[S ou N]: ").upper()
    
    if pg_s_n== "S": # Caso o usuario deseje adicionar mais um numero, retorna para a solicitação
        continue
    
    if pg_s_n=="N":
        valores_digitados = ", ".join(map(str, sorted(num))) # Tratamento para remover os colchetes
        print(f"Os valores digitados são: {valores_digitados}")
        break
    else:
        print("Valor digitado, inválido, digite novamente!")
        continue