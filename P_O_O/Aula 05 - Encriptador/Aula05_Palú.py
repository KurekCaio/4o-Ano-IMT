from string import ascii_uppercase,digits,punctuation,whitespace

d = {}

letras = ascii_uppercase
digitos = digits
pontuacao = punctuation
espacos = whitespace

dicionario_novo = {}

def cria_dicionario(dicionario_novo):

    i = 0
    print("\nPara cada uma das letra do alfabeto, digite a letra que será na sua criptografia")
        
    while i < 26:
            
        letra_nova = ""
            
        while len(letra_nova) != 1:
                
            letra_nova = input("\nPara a letra " + letras[i] + ": ").upper()
                
            if len(letra_nova) != 1:
                print("\nDigite exclusivamente um caractere!!!")
    
        if letra_nova in digitos:
            print("\nEsse valor já está em no dicionário dos números!")
                           
        elif letra_nova in pontuacao:
            print("\nEsse valor já está em no dicionário das pontuações!")
    
        elif letra_nova in espacos:
            print("\nEsse valor já está em no dicionário dos espaços!")
 
        elif letra_nova == "Ç":
            print("\nEsse caracter da xabu, bro...")
                
        elif letra_nova not in dicionario_novo.values():
            dicionario_novo[letras[i]] = letra_nova
            i+=1
                
        else:
            print("\nVocê já adicionou esse valor")
                
    print("\nSeu dicionário ficou assim:\n",dicionario_novo)
    
def criptografia(dicionario_novo):
    
    frase = input("\nDigite a frase que deseja criptografar:\n").upper()
    frase_criptografada = ""
    
    for letra in frase:
        
        if letra in dicionario_novo:
            frase_criptografada += dicionario_novo[letra]
        
        else:
            frase_criptografada += letra
                    
    print("\nFrase digitada = ", frase)
    print("Frase criptografada = ", frase_criptografada)
    
    return frase_criptografada
    
def descriptografia(frase_criptografada):
       
    lista_chaves = list(dicionario_novo.keys())
    lista_valores = list(dicionario_novo.values())
    
    frase_descriptografada = ""
    
    for letra in frase_criptografada:
        
        if letra in dicionario_novo:
            frase_descriptografada += lista_chaves[lista_valores.index(letra)]
            
        else:
            frase_descriptografada += letra
            
            
    print("Frase descriptografada = ", frase_descriptografada)
            
cria_dicionario(dicionario_novo)
x = criptografia(dicionario_novo)
descriptografia(x)
