n = int(input("Digite um número para que seja exibido o seu antecessor e sucessor:"))

sub = n - 1
a = n + 1

print("O antecessor de {} é {} e o seu sucessor é {}, correto?".format(n,sub, a))

print("Responda com (sim) ou (não) abaixo")
r = input("Responda aqui por favor:")

if r == "sim":
    print("Fico feliz em estar correto")

else:
    print("Lamento em estar errado")
  