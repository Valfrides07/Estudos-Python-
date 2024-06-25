m = float(input("Informe aqui, lembrando que o uso da virgula(,) deve ser trocado pelo uso do ponto (.):"))
u = float(input("A ultima nota:"))

media = m + u
media_final = media/2

print(f"A sua média é de:{media_final:.2f}".format(media_final))

if media_final <=4.9:
     print("Reprovado")
     
else:
    print("Aprovado, parábens!")