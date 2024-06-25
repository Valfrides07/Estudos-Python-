#Um Algoritmo que informe a média de tres alunos, média abaixo de: 5.0 (reprovado), entre 5.0 e 6.9(recuperação) e acima de 7.0(aprovado).

media_01 = float(input("Insira a sua média: "))
media_02 = float(input("Insira a sua média: "))

#calculo de media, para determinar se esta aprovado, recuperção ou reprovado

calculo_media = (media_01 + media_02) / 2

#determinação

if calculo_media >= 7.0:
    print("Parábens aluno, voce se saiu muito bem, está aprovado!!")

elif calculo_media <= 4.9: 
   print("A sua nota esta abaixo do necessário para ser aprovado, por tanto voce esta reprovado.") 

else:
    print("Voce obteve uma boa nota porem, não o sufuciente para ser aprovado diretamente, por tanto esta de recuperação")


  
