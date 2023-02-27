# Calculadora



while(True):
    print("===========================================")
    print("\t\tCalculadora")
    print("===========================================")
    print(" 0 → Sair\n 1 → Soma:\t\tx + y\n 2 → Subtração:\t\tx - y\n 3 → Multiplicação:\tx * y\n 4 → Divisão:\t\tx / y\n 5 → Raiz Quadrada:\tx^(1/2)")
    Op = int(input("Digite um número para a opção desejada:"))

    if (Op < 1 or Op > 5):
        break

    x = complex(input("Primeiro número: "))
    if Op != 5:
        y = complex(input("Segundo número: "))

    match Op:
        case 1:
            res = x + y
        case 2:
            res = x - y
        case 3:
            res = x * y
        case 4:
            res = x / y
        case 5:
            res = x^(1/2)

    if res.imag == 0:
        print("-------------")
        print("Resposta: %.5f" %res.real)
        print("-------------")
    else:
        print("-------------")
        print("Resposta: %.5f + %.5fj" %(res.real, res.imag))
        print("-------------")
