#Importacao de bibliotecas
import operator

#Definicao das funcoes
def Menu():
    "Inicializa a calculadora e permite a escolha da operacao desejada"
    
    print('Calculadora Ligada... \n')
    operacao = int(input('''
Escolha a operacao desejada:
1. Adicao
2. Subtracao
3. Multiplicacao
4. Divisao
5. Radiciacao

>> '''))

    return operacao


def Calculadora():
    "Realiza a operacao e apresenta o resultado"
    
    op = Menu()
    
    ops = {
        1: operator.add,
        2: operator.sub,
        3: operator.mul,
        4: operator.truediv,
        5: operator.pow
        } 
        
        
    if 1 <= op <= 4:
    
        Termo1 = complex(input('Digite o primeiro termo da operacao: '))
        Termo2 = complex(input('Digite o segundo termo da operacao: '))
        
        res = ops[op](Termo1,Termo2)
        print("\nResultado = {}".format(res))
    
    
    elif op == 5:
        Termo1 = complex(input('Digite o termo da operacao: '))
        res = ops[op](Termo1,(1/2))
        print("\nResultado = {}".format(res))
        
        
    else:
        print('Erro! Digite um valor valido\n')

    NovoCalculo()


def NovoCalculo():
    "Verifica se o usuario dejesa ou nao realizar outro calculo"
    
    Novo = input('''
Quer efetuar mais um calculo?
(S) Sim
(N) Nao

>> ''')

    if Novo.upper() == 'S':
        Calculadora()
    elif Novo.upper() == 'N':
        print('Calculadora Desligada.')
    else:
        print("Opcao invalida! Digite apenas 'S' ou 'N'")
        NovoCalculo()


#Programa Principal
Calculadora()
