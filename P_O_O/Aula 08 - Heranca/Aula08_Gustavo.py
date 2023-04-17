class Dispositivo():
    def __init__(self,nome,ID=0):
        self.nome = nome
        self.ID = ID
        
    def returnID(self):
        return str(self.ID)
    
class Atuador(Dispositivo):
    def __init__(self, nome, ID, estado):
        super().__init__(nome,ID)
        self.estado = estado
        
    def exibeEstado(self):
        if(self.estado==1):
            print("Atuador Ligado")
        else:
            print("Atuador Desligado")
    
class LED(Atuador):
    def __init__(self, nome, ID, estado):
        super().__init__(nome,ID, estado)
    
    def liga(self):
        self.estado = 1
        
    def desliga(self):
        self.estado = 0
    
class Motor(Atuador):
    def __init__(self, nome, ID):
        super().__init__(nome,ID,0)
        self.direcao = 0
        self.velocidade = 0
        
    def atribuiDirecao(self, estado):
        self.direcao = estado
        
    def atribuiVelocidade(self, velo):
        self.velocidade = velo
        if(velo>0):
            self.estado = 1
        else:
            self.estado = 0
        

    
x = Motor("motor amarelo",99)
x.atribuiVelocidade(9)

x.exibeEstado()
print(x.returnID())
