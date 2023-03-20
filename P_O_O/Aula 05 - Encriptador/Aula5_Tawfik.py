
from string import *

def encriptar(frase, conversor):
    fraseEncriptada = ""
    for i in frase:
        if i in conversor:
            i = conversor[i]
        fraseEncriptada += i
    return fraseEncriptada

def desencriptar(frase, conversor):
    fraseDesencriptada = ""
    dKeys = list(conversor.keys())
    dValues = list(conversor.values())
    for i in frase:
        if i in dValues:
            i = dKeys[dValues.index(i)]
        fraseDesencriptada += i
    return fraseDesencriptada

def caracteres():
    d = {}
    dKeys = list(d.keys())
    for letra in ascii_uppercase:
        dValues = list(d.values())
        d[letra] = input(f"Qual valor correspondente a {letra}: ").lower()
        while (d[letra] in dValues) or (len(d[letra]) != 1):
            d[letra] = input(f"Qual valor correspondente a {letra}: ").lower()
    # for letra in digits:
    #     dValues = list(d.values())
    #     d[letra] = input(f"Qual valor correspondente a {letra}: ").lower()
    #     while (d[letra] in dValues) or (len(d[letra]) != 1):
    #         d[letra] = input(f"Qual valor correspondente a {letra}: ").lower()
    # for letra in punctuation:
    #     dValues = list(d.values())
    #     d[letra] = input(f"Qual valor correspondente a {letra}: ").lower()
    #     while (d[letra] in dValues) or (len(d[letra]) != 1):
    #         d[letra] = input(f"Qual valor correspondente a {letra}: ").lower()
    # for letra in whitespace:
    #     dValues = list(d.values())
    #     d[letra] = input(f"Qual valor correspondente a {letra}: ").lower()
    #     while (d[letra] in dValues) or (len(d[letra]) != 1):
    #         d[letra] = input(f"Qual valor correspondente a {letra}: ").lower()
    return d

        

# conversor = {'8': '8', 'C': 'e', 'Y': 'n', 'U': 'x', 'G': 'u', 'Q': 'j', '^': '^', "'": "'", '~':
# '~', 'Z': 'm', '/': '/', 'R': 'k', '+': '+', 'E': 't', 'D': 'r', '|': '|', 'K': 'a', '1': '1',
# '?': '?', 'O': 'g', '\x0b': '\x0b', 'I': 'o', '4': '4', '(': '(', 'A': 'q', '.': '.', '{': '{',
# '!': '!', '\r': '\r', ']': ']', '0': '0', '-': '-', 'B': 'w', '}': '}', '$': '$', 'S': 'l', 'W':
# 'v', 'V': 'c', 'F': 'y', '7': '7', ';': ';', ' ': ' ', '*': '*', ')': ')', '%': '%', '#': '#',
# '9': '9', '@': '@', '6': '6', '>': '>', '\\': '\\', '=': '=', '\x0c': '\x0c', 'H': 'i', 'M': 'd',
# 'J': 'p', ',': ',', '<': '<', 'L': 's', '5': '5', 'P': 'h', 'X': 'b', '\t': '\t', '&': '&', '`':
# '`', ':': ':', 'N': 'f', '\n': '\n', '_': '_', '3': '3', '[': '[', '2': '2', 'T': 'z', '"': '"'}

# fraseOriginal = """PREPAREM-SE PARA A ENCRENCA!
# ENCRENCA EM DOBRO!
# PARA PROTEGER O MUNDO DA DEVASTACAO!
# PARA UNIR AS PESSOAS DE NOSSA NACAO!
# PARA DENUNCIAR OS MALES DA VERDADE E DO AMOR!
# PARA ESTENDER O NOSSO PODER AS ESTRELAS!
# JESSE!
# JAMES!
# EQUIPE ROCKET DECOLANDO NA VELOCIDADE DA LUZ!
# RENDA-SE AGORA OU PREPAREM-SE
# PARA LUTAR!"""

fraseOriginal = input("Digite a frase para encriptar: ")

# novaFrase = """hkthqktd-lt hqkq q tfektfeq!
# tfektfeq td rgwkg!
# hqkq hkgztutk g dxfrg rq rtcqlzqeqg!
# hqkq xfok ql htllgql rt fgllq fqeqg!
# hqkq rtfxfeoqk gl dqstl rq ctkrqrt t rg qdgk!
# hqkq tlztfrtk g fgllg hgrtk ql tlzktsql!
# ptllt!
# pqdtl!
# tjxoht kgeatz rtegsqfrg fq ctsgeorqrt rq sxm!
# ktfrq-lt qugkq gx hkthqktd-lt
# hqkq sxzqk!"""

#print('A' in conversor)
conversor = caracteres()
novaFrase = encriptar(fraseOriginal, conversor)
print(f"frase encriptada: {novaFrase}")
print(f"frase desencriptada: {desencriptar(novaFrase, conversor)}")