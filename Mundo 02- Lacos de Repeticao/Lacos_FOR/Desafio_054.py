#Um laço que leia a idade de 7 pessoas e informe se já chegaram a maior idade, levando em consideração que a a maior idade deve ter mais de 21 anos

#contador, para armazenar pessoas maiores e menores de idades
idademaior = 0
idademenor = 0

for i in range(1,8):
    idade = int(input(f"Insira o ano {i}º de nascimento: "))
    cal_idade = 2024 - idade
    if cal_idade >= 18:
        
        #Se for maior de idade vai contabilizar mais 1
        idademaior += 1
        
        #Se for menor de idade vai contabilizar mais 1
    else:
        idademenor += 1

print(f"A quantidade de pessoas maiores de idades são de: {idademaior}")
print(f"A quantidade de pessoas menores de idades são de: {idademenor}")