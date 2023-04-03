class Cliente():
    def __init__(self, nome, CPF):
        self.nome = nome
        self.__CPF = CPF
        self.__saldo = 0
        self.__limite = 1500
        
        
    def exibeCPF(self):
        print(self.nome)
    
    def exibeSaldo(self):
        print(self.__saldo)
        
    def deposita(self,i):
        self.__saldo += i
    
    def pagamento(self, i):
        if (self.__saldo-i < -self.__limite):
            print("erro ao realizar pagamento, limite insuficiente")
        else:
            self.__saldo -= i
        
palu = Cliente("Matheus Palu", 12345678910)

palu.deposita(150)
palu.pagamento(1000)
palu.exibeSaldo() 
