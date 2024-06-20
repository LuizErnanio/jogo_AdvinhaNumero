import random

numeroRespostas = 3
numeroAleatorio = random.randint(1, 10)


#fazer um laço de repetição
while True:
    numeroDigitado = input("Digite um numero aqui!")
    numeroRespostas -= 1
    if numeroDigitado == numeroAleatorio:
        print("Você acertou!")
    else:
        print("Você errou!")
        if numeroRespostas == 0:
            break


#colocar um numero random e definir a limitação de numeros tanto de tentativa como opção de resposta.
#quando acertar o usuario recebe uma mendagem de acerto, o mesmo acontece após as 3 tentativas erradas, mas com uma mensagem que ele perdeu.
 