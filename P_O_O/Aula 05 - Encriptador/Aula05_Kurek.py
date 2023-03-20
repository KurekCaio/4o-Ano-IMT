# Encriptador

from string import *

def encriptar(frase, conversor) :
    for letra in frase:
        letra = conversor[letra]
        print(letra,end="")

def desincriptar(frase, conversor) :
    dKeys = list(conversor.keys())
    dValues = list(conversor.values())
    for letra in frase:
        letra = dKeys[dValues.index(letra)]
        print(letra,end="")

def converter() :
    d = {}
    for letra in ascii_uppercase:
        dKeys = d.keys()
        dValues = d.values()
        caractere = input("Digite a letra que corresponde a %s: " %(letra)).lower()
        while (len(caractere) != 1) or (caractere in dValues):
            caractere = input("VALOR INVALIDO!! Digite UM caractere unico que corresponde a %s: " %(letra)).lower()
        d[letra] = caractere
    return d
    
    print(d)

#Inicio do Programa
d = converter()
while (1) :
    fraseEncriptada = input("Digite a frase que deseja encriptar: ")
    encriptar(fraseEncriptada,d)
    desincriptar(fraseEncriptada,d)



