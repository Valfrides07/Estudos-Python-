# 1- Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(n):
    numero = [0, 1]
    while len(numero) < n:
        numero.append(numero[-1] + numero[-2])
    return numero[:n]

n = int(input('Digite um número: '))
print(fibonacci(n))


# 2- Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def verificacao(a, A, palavra):
    if A in palavra:
        print(f'A palavra {palavra} contém a letra {A}.')
        
    elif a in palavra:
        print(f'A palavra {palavra} contém a letra {a}.')
        
    else:
        print('A palavra não contém a letra A .')

palavra = input('Digite uma palavra: ')
palavra.upper
print (verificacao('a','A', palavra))

# 3- Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

# 5- Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

class Lampada:
    def __init__(self, id):
        self.id = id
        self.estado = "fria"  

    def ligar(self):
        self.estado = "ligada"

    def desligar(self):
        if self.estado == "ligada":
            self.estado = "quente"
        else:
            self.estado = "fria"

    def verificar_estado(self):
        return self.estado

lampadas = [Lampada(1), Lampada(2), Lampada(3)]

def descobrir_interruptores():

    lampadas[0].ligar()

    lampadas[0].desligar()

    lampadas[1].ligar()

    for lampada in lampadas:
        estado = lampada.verificar_estado()
        print(f"Lâmpada {lampada.id} está {estado}.")

descobrir_interruptores()
