import random
from string import *

conversor = {'8': '8', 'C': 'e', 'Y': 'n', 'U': 'x', 'G': 'u', 'Q': 'j', '^': '^', "'": "'", '~':
'~', 'Z': 'm', '/': '/', 'R': 'k', '+': '+', 'E': 't', 'D': 'r', '|': '|', 'K': 'a', '1': '1',
'?': '?', 'O': 'g', '\x0b': '\x0b', 'I': 'o', '4': '4', '(': '(', 'A': 'q', '.': '.', '{': '{',
'!': '!', '\r': '\r', ']': ']', '0': '0', '-': '-', 'B': 'w', '}': '}', '$': '$', 'S': 'l', 'W':
'v', 'V': 'c', 'F': 'y', '7': '7', ';': ';', ' ': ' ', '*': '*', ')': ')', '%': '%', '#': '#',
'9': '9', '@': '@', '6': '6', '>': '>', '\\': '\\', '=': '=', '\x0c': '\x0c', 'H': 'i', 'M': 'd',
'J': 'p', ',': ',', '<': '<', 'L': 's', '5': '5', 'P': 'h', 'X': 'b', '\t': '\t', '&': '&', '`':
'`', ':': ':', 'N': 'f', '\n': '\n', '_': '_', '3': '3', '[': '[', '2': '2', 'T': 'z', '"': '"'}

def criar_caracteres():
    if (True):
        return conversor
        
    caracteres = ascii_uppercase + digits
    dicionario = {}
    for i in range(len(caracteres)):
        x = input("Adicionar um caracter unico para ["+caracteres[i]+"]: ").lower()
        
        while(x in list(dicionario.values())):
            x = input("Adicionar um CARACTER UNICO para ["+caracteres[i]+"]: ").lower()
            
        dicionario[caracteres[i]] = x
    
    print(dicionario)
    return dicionario

def encriptar(frase, dicionario):
    frase_encriptada = ""
    for letra in frase:
        if letra in dicionario.values():
            for chave, valor in dicionario.items():
                if valor == letra:
                    frase_encriptada += chave
        else:
            frase_encriptada += letra
    return frase_encriptada

def decriptar(frase_encriptada, dicionario):
    frase_decriptada = ""
    for letra in frase_encriptada:
        if letra in dicionario.keys():
            frase_decriptada += dicionario[letra]
        else:
            frase_decriptada += letra
    return frase_decriptada


while True:
       
    caracteres_encriptacao = criar_caracteres()
    print("Caracteres de encriptação:", caracteres_encriptacao)
    
    frase_original = input("Digite a frase a ser encriptada: ")
    
    frase_encriptada = encriptar(frase_original, caracteres_encriptacao)
    print("Frase encriptada:", frase_encriptada)
    
    frase_decriptada = decriptar(frase_encriptada, caracteres_encriptacao)
    print("Frase decriptada:", frase_decriptada)
    
    if frase_original == frase_decriptada:
        print("A frase decriptada é igual à frase original.")
    else:
        print("A frase decriptada é diferente da frase original.")
