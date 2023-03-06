from math import *
import cmath

def soma(x,y):
    return (x+y)

def subtrai(x,y):
    return x-y

def multiplica(x,y):
    return x*y

def divide(x,y):
    return x/y

def raiz(x):
    return cmath.sqrt(x)

while(True):
    opcao = int(input("""------------Calculadora--------------
    Escolha uma das opções abaixo:
    1 Soma             2 Subtração
    3 Multiplicação    4 Divisão
    5 Raiz quadrada    6 Sair
    Opção: """))
    resp = 0
    if(opcao < 1 or opcao > 5):
        break
    x = complex(input("Digite o primeiro número: "))
    if(opcao != 5):
        y = complex(input("Digite o segundo número: "))


    match opcao:
        case 1:
            print("Sua soma é: ")
            resp = soma(x,y)
        case 2:
            print("Sua subtração é: ")
            resp = subtrai(x,y)
        case 3:
            print("Sua multiplicação é: ")
            resp = multiplica(x,y)
        case 4:
            print("Sua divisão é: ")
            resp = divide(x,y)
        case 5:
            print("Sua raiz quadrada é: ")
            resp = raiz(x.real)

    if(resp.imag == 0):
        print("%.3f" %resp.real)
    else:
        print("%.3f + %.3fj" %(resp.real, resp.imag))
