# Faça um programa nome e peso de varias pessoas,guardando tudo dentro de uma lista e no final mostre: quantas pessoas foram cadastradas, uma listagem com as pessoas mais pesadas e uma listagem com  as pessoas mais leves.

qnt_pessoas = []
nome_lista = []
peso_baixo = []
peso_baixo = []

while True:
    nome = str(input("Ensira o seu nome: "))
    nome_lista.append(nome)
    con = str(input("Deseja enserir mais um nome? "))
    if con == "sim" or con == "s":
        continue

    if con == "nao" or con == "n":
        break