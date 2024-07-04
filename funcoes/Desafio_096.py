# Faça um programa que tenha uma função (def) chamada area()  que receba as dimensoes de um terreno retangular( largura e comprimento) e mostre a area do terreno

largura_0= []
comprimento_0=[]

# def é uma palavra-chave usada para definir uma função,que realiza uma tarefa específica geralmente inclui um nome, parâmetros (opcionais), e um bloco de código que será executado quando a função for chamada.
def area(Largura, comprimento):
    calculo = Largura * comprimento # A função dessa def
    print(f"A area do terreno é: {calculo:.0f}m²")

while True:
    largura = float(input("Informe a largura em metros: "))
    largura_0.append(largura)

    comprimento = float(input("Informe o comprimento em metros: "))
    comprimento_0.append(comprimento)
    pgt = str(input(f"As medidas digitadas estão corretas? Largura e Comprimento {largura_0} x {comprimento_0}m²:")).lower()

    if pgt == "n" or pgt == "nao":
        continue

    if pgt == "sim" or pgt == "s":
        area(largura,comprimento) # Precisa chamar a função area com os parâmetros largura e comprimento.
        break
    
    else:
        print("Informação inválida, ensira novamente.")
        continue