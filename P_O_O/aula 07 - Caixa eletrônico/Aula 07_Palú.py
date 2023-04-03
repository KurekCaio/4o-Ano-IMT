#Programa do Caixa Eletrônico

print("\nBEM VINDO AO CAIXA ELETRÔNICO\n")

class Cliente:
    
    def __init__(self, Nome, CPF, Saldo = None, Limite = None):
        self.Nome = Nome
        self.__CPF = CPF
        self.__saldo = 0
        self.__limite = 1000
        
    def exibeNome(self):
        print("O nome do cliente é:",self.Nome)
        return self.Nome
        
    def exibeCPF(self):
        print("O CPF do cliente é:",self.__CPF)
        return self.__CPF
    
    def exibeSaldo(self):
        print("O saldo do cliente é %i reais"%self.__saldo)
        return self.__saldo
        
    def exibeLimite(self):
        print("O limite do cliente é de %i reais"%self.__limite)
        return self.__limite
        
    def deposito(self, valor):
        self.__saldo += valor
        print("O valor do depósito é de %i reais"%valor)
        
    def pagamento(self, valor):
        if (self.__saldo + self.__limite) >= valor:
            self.__saldo -= valor
            print("Pagamento de %i reais"%valor)
        else: 
            print("Você está querendo usar mais do que você pode, amigão...")
        
cliente_Palú = Cliente("Matheus Ferreira Palú","450.615.128-39")

print("\nDADOS INICIAIS:\n")
cliente_Palú.exibeNome()
cliente_Palú.exibeCPF()
cliente_Palú.exibeSaldo()
cliente_Palú.exibeLimite()

print("\nDADOS D0 DEPÓSITO 1:\n")
cliente_Palú.deposito(100)
cliente_Palú.pagamento(1200)

print("\nDADOS FINAIS 1:\n")
cliente_Palú.exibeSaldo()
cliente_Palú.exibeLimite()

print("\nDADOS DO DEPÓSITO 2:\n")
cliente_Palú.deposito(200)
cliente_Palú.pagamento(500)

print("\nDADOS FINAIS 2:\n")
cliente_Palú.exibeSaldo()
cliente_Palú.exibeLimite()
