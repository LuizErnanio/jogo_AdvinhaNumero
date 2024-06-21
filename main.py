import random

while True:
    numeroRespostas = 3
    numeroAleatorio = random.randint(1, 10)
    while True:
        numeroDigitado = int(input("Digite um numero aqui!"))
        numeroRespostas -= 1
        if numeroDigitado == numeroAleatorio:
            print("Você acertou!")
            break            
        else:        
            if numeroRespostas == 0:
                print("Você esgotou suas chances!")
                break
            else: 
                print(f"Você errou! tem mais {numeroRespostas} tentaivas.")
    tentarNovamente = int(input("Gostaria de tentar novamente? digite 1 para SIM e 2 para NÃO"))
    if tentarNovamente == 2:
        print("Jogo finalizado!")
        break 