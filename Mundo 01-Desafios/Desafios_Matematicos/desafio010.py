print("Para calcularmos a quantidade de dólares que possivelmente voce pode comprar me informe os Reais que voce possue, abaixo")
r = float(input("Digite aqui por favor:"))

c = r/5.12

if r<=5.11:
    print("Infelizmente voce não posssue a quantidade suficente de Reais para comprar dólares.") 
    
else:
    c_rounded = round(c,2)
    print(f"A quantidade de dólares que pode comprar é essa:{c_rounded} USD".format(c))

