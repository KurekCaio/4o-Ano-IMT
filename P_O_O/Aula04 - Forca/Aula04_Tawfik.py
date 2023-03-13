from random import choice
import os

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

    print("\nLetras erradas:",erradas)
    print("Letras corretas:",certas)

def iniciaPalavra(tamanho):
    return '_'*tamanho

def sorteia():
    return choice(['cachorro', 'gato', 'galinha', 'cavalo', 'camelo', 'girafa', 'elefante', 'pirata', 'rato', 
        'arara', 'arame', 'familia', 'camisa', 'fazenda', 'cama', 'mesa', 'garfo', 'sapato', 'formiga', 'martelo',
         'lagarto', 'lanche', 'copo', 'corpo', 'humano', 'laranja', 'pera', 'melancia', 'manteiga', 'sofa'])

secreta = sorteia()
print(secreta)
palavra = iniciaPalavra(len(secreta))

ponto = 0
certas = []
erradas = []
i = []



while (ponto < 6) and (len(certas) != len(palavra)):
    imprime(ponto, certas, erradas, palavra)
    chute = input("Chuta uma letra: ").lower()
    
    if chute in secreta:
        if chute in certas:
            print("BURRO!! REPETIU A PALAVRA!! NÃO MERECE CONTINUAR JOGANDO!!")
            break
        else:
            certas.append(chute)
            for letra in secreta:
                i = secreta.index(chute)
                palavra = palavra[:i]+chute+palavra[i+1:]
    else:
        if chute in erradas:
            print("BURRO!! REPETIU A PALAVRA!! NÃO MERECE CONTINUAR JOGANDO!!")
            break
        else:
            erradas.append(chute)
            ponto+=1

#print(len(certas))
#print(len(palavra))
#print(ponto)
print(f"A palavra era: {secreta}")
os.system('pause')

