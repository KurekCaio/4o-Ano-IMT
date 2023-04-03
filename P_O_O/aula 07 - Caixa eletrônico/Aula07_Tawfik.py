class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf
        self.__saldo = 0
        self.__limite = 200
    def exibeCPF(self):
        print(self.__cpf)
    def exibeSaldo(self):
        print(self.__saldo)
    def deposito(self, valor):
        self.__saldo += valor
    def pagamento(self, valor):
        if(self.__saldo - valor < -self.__limite):
            print("Erro! Saldo + Limite insuficiente!")
        else:
            self.__saldo -= valor        

user = Cliente("PADS SDHSDK", "123.456.789-10")
user.exibeCPF()
user.deposito(150)
user.pagamento(350)
user.exibeSaldo()