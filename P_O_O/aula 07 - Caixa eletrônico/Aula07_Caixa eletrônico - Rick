class Cliente:
    def __init__(self, nome, CPF, saldo = None, limite = None):
        self.nome = nome
        self.__CPF = CPF
        self.__saldo = 0
        self.__limite = 3000
        print("Bem vindo ao caixa eletrônico do Brasil colonial\n\n")
        
    
    def exibeCPF(self):
        print("CPF: ", self.__CPF)
    
    def exibeSaldo(self):
        print("Saldo atual: {0} réis".format(self.__saldo))
    
    def deposito(self, valor):
        self.__saldo += valor
        print("Deposito de: {0} réis\n".format(valor))
    
    def pagamento(self, valor):
        if (self.__saldo + self.__limite) >= valor:
            self.__saldo -= valor
            print("Pagamento de {0} réis aprovado\n".format(valor))
        else:
            print("Tentativa de pagamento falhou!\nVoce eh a vergonha da familia real portuguesa!\nSeu limite eh {0}\n".format(self.__limite))
      
        
cliente01 = Cliente("Dom Pedro II", "000.000.000-01")

print("Nome: ", cliente01.nome)

cliente01.exibeCPF()
cliente01.exibeSaldo()

cliente01.deposito(300)
cliente01.pagamento(4000)

cliente01.exibeSaldo()
cliente01.deposito(1000)
cliente01.pagamento(4000)

cliente01.exibeSaldo()



