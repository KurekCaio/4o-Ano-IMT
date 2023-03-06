import random

print("**************************************")
print("* Bem-vindos ao jogo da adivinhacao! *")
print("**************************************")
print ("Tente acertar o número secreto de 1 a 99!")
print("Regras: Somente número ACIMA DE ZERO e escolha uma das opções abaixo.")
print("Escolha o seu nivel de dificuldade:")
print("Facil (F), Medio (M) ou Dificil (D)")

dificuldade = input().upper()

if dificuldade == 'F':
    numero_de_tentativas = 15
elif dificuldade == 'M':
    numero_de_tentativas = 10
elif dificuldade == 'D':
    numero_de_tentativas = 5
else:
    print("Você digitou uma opção inviálda!")
    exit(0)
    
print(f"Você tem {numero_de_tentativas} tentativas!")
NUMERO_SECRETO = random.randint(1, 99)

nao_acertou = True
tentativas = 0
pontos = 1000.0

for tentativas in range(1, numero_de_tentativas + 1):
    print(f"Tentativa {tentativas}")
    chute = input("Qual seu chute? ")
    if chute.isdigit():
        chute = int(chute)
        pontos_perdidos = abs(chute - NUMERO_SECRETO) / 2.0
        pontos -= pontos_perdidos
    else:
        print("Você digitou um número inválido! Por favor respeite as regras senão você nunca vai terminar o jogo!!")
        exit(0)

    print(f"O valor do seu chute eh: {chute}")
    acertou = chute == NUMERO_SECRETO
    maior = chute > NUMERO_SECRETO

    if acertou:
        print("Parabens! Voce acertou o numero secreto!")
        nao_acertou = False
        break
    elif maior:
        print("Seu chute foi maior que o numero secreto!")
    else:
        print("Seu chute foi menor que o numero secreto!")

print("Fim de jogo!")
if nao_acertou:
    print("Voce perdeu! Tente novamente!")
else:
    print(f"Voce acertou o numero secreto em {tentativas} tentativas")
    print(f"Sua pontuacao foi de {pontos:.2f} pontos.")