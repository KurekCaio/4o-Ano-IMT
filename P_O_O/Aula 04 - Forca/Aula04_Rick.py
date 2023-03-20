#Importacao das bibliotecas
from random import choice
import os

#Definicao das funcoes
def imprime(ponto, certas, erradas, palavra):
    #os.system('cls')
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

#Programa principal
secreta = sorteia()
print(secreta)

ponto = 0
certas = []
erradas = []
palavra = iniciaPalavra(len(secreta))

letra = []


while (ponto < 6) and (palavra != secreta):
    imprime(ponto, certas, erradas, palavra)
    palpite = input("\nQual e o seu palpite? ")
    
    
    if palpite in secreta:
        if palpite not in certas:
            certas.append(palpite)
            
            
            for letra in range(len(secreta)):
                if secreta[letra] == palpite:
                    palavra = palavra[:letra]+palpite+palavra[letra+1:]
                
        else:
            print("\n\nJa deu esse palpite\n")
            
    else:
        if palpite not in erradas:
            erradas.append(palpite)
            ponto += 1
        else:
            print("\n\nJa deu esse palpite\n")


if palavra == secreta:
    print("Parabens, você acertou a palavra secreta!")

else:
    print("Não foi dessa vez! A palavra era secreta era {}".format(secreta))

os.system('pause')
