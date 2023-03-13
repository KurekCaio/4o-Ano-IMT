import os
from random import choice

def imprime(ponto, certas, erradas, palavra):
    os.system('cls')
    print("*************** Forca ***************")
    print("\n\nPalavra secreta: " + palavra + "\n\n")
    if(ponto == 0):
        print("=======[_] \n||      |  \n||         \n||         \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 1):
        print("=======[_] \n||      |  \n||      o  \n||         \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 2):
        print("=======[_] \n||      |  \n||      o  \n||      |  \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 3):
        print("=======[_] \n||      |  \n||      o  \n||     /|  \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 4):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 5):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||     /   \n||         \nHHHHHHHHHHHH")
    elif(ponto == 6):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||     / \ \n||         \nHHHHHHHHHHHH")

    print("\nLetras erradas:", erradas)
    print("Letras corretas:", certas)

def iniciaPalavra(tamanho):
    return '_'*tamanho

def sorteia():
    return choice(['cachorro', 'gato', 'galinha', 'cavalo', 'camelo', 'girafa', 'elefante', 'pirata', 'rato', 
        'arara', 'arame', 'familia', 'camisa', 'fazenda', 'cama', 'mesa', 'garfo', 'sapato', 'formiga', 'martelo',
         'lagarto', 'lanche', 'copo', 'corpo', 'humano', 'laranja', 'pera', 'melancia', 'manteiga', 'sofa'])

palavra = sorteia()
palavra_atual = iniciaPalavra(len(palavra))
letras_certas = []
letras_erradas = []
tentativas = 0

while tentativas < 6:
    #print("os iniciallllll")
    imprime(tentativas, letras_certas, letras_erradas, palavra_atual)
    letra = input('Digite uma letra: ').lower()

    if letra in letras_certas or letra in letras_erradas:
        print('Você já tentou essa letra antes. Tente outra.')
        continue    

    if letra in palavra:
        letras_certas.append(letra)
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_atual = palavra_atual[:i] + letra + palavra_atual[i+1:]
    else:
        letras_erradas.append(letra)
        tentativas += 1

    if '_' not in palavra_atual:
        print("os acabou ___")
        #os.system('cls')
        #imprime(tentativas, letras_certas, letras_erradas, palavra_atual)
        print('\nvocê acertou a palavra:', palavra)
        break

    if tentativas == 6:
        print("os acbou as tentavis")
        #os.system('cls')
        #imprime(tentativas, letras_certas, letras_erradas, palavra_atual)
        print('\nPerdeu, a palavra era:', palavra)
        break
    os.system("pause")