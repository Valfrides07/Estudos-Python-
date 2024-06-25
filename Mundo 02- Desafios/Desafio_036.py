#Recebimento de informações para o financiamento

casa_valor = float(input("Por favor, informe o valor da casa: "))
salario_valor = float(input("Por favor, informe o seu sálario: "))
anos_financiamento = int(input("Por favor, informe em quantos anos deseja quitar o financiamento: "))

#Calculo entre salario e anos, para saber se é possivel fazer financiamento

calculo_meses = anos_financiamento * 12
conversao = casa_valor / calculo_meses

#Não podendo exceder em 30% do salário mensal

excedencia_salario = salario_valor * 0.3

#Confirmação de dados

confirmacacao = str(input(f"Confirme para mim se os dados estão corretos, o valor da casa é de {casa_valor:.3f} reais, salário é {salario_valor:.3f} reais e a quantidade de anos de financiamento são {anos_financiamento} anos?" .format(casa_valor,salario_valor)))
sim_ou_nao = str(input("responda com SIM ou NAO: ")) 

if sim_ou_nao == ("NAO"):
    print("Por favor, refaça com os dados corretos.")

else: sim_ou_nao == ("SIM")
print("Já estamos finalizando, para que possa ser liberado ou não o seu financiamento!!")

#Agora mostrar se o financiamento foi aprovado ou não

if conversao > excedencia_salario :
       nome_usuario = str(input("Me informe o seu Nome, por gentileza: "))
       print("Infelizmente {} a sua renda atual não permite que financie uma casa desse valor." .format(nome_usuario))

else:
      nome_usuario = str(input("Me informe o seu Nome, por gentileza: "))
      print(f"Parabens {nome_usuario}, voce se encaixa nas condições de financiamento da casa. A quantidade de parcelas são de: {calculo_meses} meses e o valor é de cada uma é: {excedencia_salario:.3f} reais.")



      