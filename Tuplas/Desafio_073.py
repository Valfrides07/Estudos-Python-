# Uma tupla que mostre uma lista dos times do brasielirao, uma lista dos 5 primeiros da tabela, uma lista dos 4 ultimos colocaddos, uma lista com os times em ordem alfabética e em qual posição esta o Fortaleza

times = ("Flamengo","Palmeiras","Bahia","Botafogo","Athletico-PR","Internacional","Cruzeiro","São Paulo","Atlético-MG","Fortaleza","Juventude","Criciúma","Cuiabá","Vasco","Atlético-GO","Vitória","Corinthians","Grêmio","Fluminense") 

print(f"Todos os times do Brasileirão: {times}") # Uma tupla que mostre uma lista dos times do brasielirao

print('-' * 200)  # Linha divisória com 40 traços

print(f"Os 5 primeiros na tabela são: {times[:5]} ") # Uma lista dos 5 primeiros da tabela

print('-' * 200)  # Linha divisória com 40 traços

print(f"Os 4 ultimos na tabela são: {times[-4:]} ") # Uma lista dos 4 ultimos colocaddos

print('-' * 200)  # Linha divisória com 40 traços

print(f"Todos os times do Brasileirão em ordem alfabética: {sorted(times)}") #Uma lista com os times em ordem alfabética

print('-' * 200)  # Linha divisória com 40 traços

for posicao, time in enumerate(times, 1):
    if time == "Fortaleza":
        print(f"E o Fortaleza se encontra na posição {posicao} na tabela.")