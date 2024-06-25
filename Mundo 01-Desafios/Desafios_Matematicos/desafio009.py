print("Digite um número qualquer entre 1 e 10, para ser exibido a sua tabuada")
n = int(input("Digite aqui:"))

mp1 = n * 1 
mp2 = n * 2 
mp3 = n * 3 
mp4 = n * 4 
mp5 = n * 5 
mp6 = n * 6 
mp7 = n * 7 
mp8 = n * 8 
mp9 = n * 9
mp10 = n * 10
 
print("Agora irei mostar a tabuada de tal número que digitado : {} , {} , {} , {} , {} , {} , {} , {} , {} , {}, ".format(mp1, mp2, mp3,mp4, mp5, mp6, mp7,mp8,mp9,mp10))

d = input(str("Agora por gentileza, informe se esta tudo correto com apenas (sim) ou (nao):"))

if d == "sim":
    print("Fico feliz por estar correto!")

else:
    print("Lamento pelo erro.")

 


