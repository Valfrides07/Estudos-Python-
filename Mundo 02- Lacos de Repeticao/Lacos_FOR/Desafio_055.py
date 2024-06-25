#Um algoritmo que leia o peso de 5 pessoas e mostre qual foi o maior peso inserido e  o menor peso

pesos = []
for pp in range(1,6):
    peso = float(input(f"Ensira o seu {pp}º peso: "))
    pesos.append(peso)

maior_peso = max(pesos)
menor_peso = min(pesos)

print(f"O maior peso informado foi de: {maior_peso} KG.")
print(f"O menor peso foi de: {menor_peso} KG.")

