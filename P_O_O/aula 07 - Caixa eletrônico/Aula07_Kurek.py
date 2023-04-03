class Cliente():
    def __init__(self, nome, CPF):
        self.nome = nome
        self.__CPF = CPF
        self.__saldo = 0
        self.__limite = 2000
        
    def exibeCPF(self):
       print("CPF: %s" %(self.__CPF))
        
    def exibeSaldo(self):
       print("Saldo atual: R$ %.2f" %(self.__saldo))
        
    def deposito(self, i) :
        self.__saldo += i
        print("Valor depositado: R$ %.2f" %(i))
        
    def pagamento(self, i):
        if (self.__saldo + self.__limite > i):
            self.__saldo -= i
            print("Valor do pagamento: R$ %.2f" %(i))
        else:
            print("ERRO! Saldo + Limite insuficiente...")
        
eu = Cliente("Caio","123.456.789-00")

eu.exibeCPF()

eu.deposito(1000)
eu.exibeSaldo()

eu.pagamento(2500)
eu.exibeSaldo()

eu.deposito(250)
eu.exibeSaldo()

eu.pagamento(2000)
eu.exibeSaldo()
