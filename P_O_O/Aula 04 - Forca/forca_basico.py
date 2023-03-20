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

