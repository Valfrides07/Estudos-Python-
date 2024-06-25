#Tabuada que mostre uma resposta de cada vez e encerre quando o número digitado for negativo

while True:
    n = int(input("Quer ver a tabuada de qual número: "))
    
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

    if n < 0:
        print("Programa finalizado.")
        break
    
    print(f"A tabuada de {n} é:\n {n} x 1: {mp1}\n {n} x 2: {mp2}\n {n} x 3: {mp3}\n {n} x 4: {mp4}\n {n} x 5: {mp5}\n {n} x 6: {mp6}\n {n} x 7: {mp7}\n {n} x 8: {mp8}\n {n} x 9: {mp9}\n {n} x 10: {mp10}")
    continue
