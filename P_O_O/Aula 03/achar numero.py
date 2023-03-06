import random

numero_secreto = random.randint(1, 100)
tentativas = 0
chutes = []

print("Adivinhe o número secreto entre 1 e 100.")

while True:
    chute_str = input("Digite um número: ")

    if not chute_str.isdigit():
        print("Digite apenas números!")
        continue

    chute = int(chute_str)
    tentativas += 1
    chutes.append(chute)

    if chute == numero_secreto:
        print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} em {tentativas} tentativa(s).")
        print("Chutes anteriores:", chutes)
        break
    elif chute < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")

    
