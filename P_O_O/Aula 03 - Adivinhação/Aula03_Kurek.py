# Jogo de adivinhação

from random import randint

print("===================")
print("Jogo de adivinhação")
print("===================")

print("\nTente adivinhar o número de 0 a 100\n")

random = randint(0,100)
chute = input("Digite o número: ")
tentativas = 0

while chute != random:
    if chute.isnumeric() == True:
        chute = int(chute)
        if 0 < chute < 100:
            if chute < random:
                tentativas += 1
                print("\nO número é maior!")
                print("Tentativas: {}".format(tentativas))
                chute = input("Digite outro numero: ")       
            elif chute > random:
                tentativas += 1
                print("\nO número é menor!")
                print("Tentativas: {}".format(tentativas))
                chute = input("Digite outro numero: ")
        else:
            print("\nDigite um numero valido entre 0 e 100!")
            chute = input("Digite outro numero: ")         
    else:
        print("\nDigite um numero valido entre 0 e 100!")
        chute = input("Digite outro numero: ")

if int(chute) == random:    
    print("\n====================================")
    print("Acertou miseravi")
    print("Voce precisou de {} tentativas".format(tentativas))
    print("====================================")
