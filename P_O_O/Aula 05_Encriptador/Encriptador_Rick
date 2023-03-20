#importacao das funcoes
from string import *

#definicao das funçoes
def CriarConversor(d, caracteres):
    for letra in caracteres:
        valor = input("Digite o caractere encriptado para '{}': ".format(letra))
        
        while(valor in d.values() or len(valor) != 1):
            if valor in d.values():
                print("\nO caractere ja foi inserido no encriptador, escolha outro.")
            else:  
                print("\nSo eh aceito um único caractere, você digitou nenhum, dois ou mais caracteres.")
            valor = input("Digite o caractere encriptado para a letra '{}': ".format(letra))
                
        d[letra] = valor
    
    print("SUCESSO! Seu dicionario de conversao foi criado.")
    
def Encriptar(frase, d):
    fraseEncriptada = ''
    for letra in frase:
        if letra in d:
            fraseEncriptada += d[letra]
        else:
            fraseEncriptada += letra
            
    return fraseEncriptada
    
def Decriptar(frase, d):
    fraseDecriptada = ''
    dKeys = list(d.keys())
    dValues = list(d.values())
    
    for letra in frase:
        if letra in d.values():
            fraseDecriptada += dKeys[dValues.index(letra)]
        else:
            fraseDecriptada += letra
    
    return fraseDecriptada
            
        

#programa principal
caracteres = ascii_uppercase + digits + punctuation + whitespace
d = {}

CriarConversor(d, caracteres)

frase = "PREPAREM-SE PARA A ENCRENCA!"
fraseEncriptada = Encriptar(frase, d)
fraseDecriptada = Decriptar(fraseEncriptada, d)

print("\n\nFrase original: ", frase)
print("Frase Encriptada: ", fraseEncriptada)
print("Frase Decriptada: ", fraseDecriptada)
        
