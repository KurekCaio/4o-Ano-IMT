class Dispositivo():
    def __init__(self, nome):
        self.nome = nome

    def retornaID(self):
        return 'Nome:' + self.nome

class Atuador(Dispositivo):
    def __init__(self, nome, estado):
        super().__init__(nome)
        self.estado = estado
        
    def exibeEstado(self):
            print(super().retornaID())
            if(self.estado == 1):
                return 'Estado: ligado'
            elif(self.estado == 0):
                return 'Estado: desligado'
    
class LED(Atuador):
    def __init__(self, nome, estado):
        super().__init__(nome, estado)
        
    def liga(self):
        self.estado = 1
        
    def desliga(self):
        self.estado = 0
    
class Motor(Atuador):
    def __init__(self, nome, estado, direcao, velocidade):
        super().__init__(nome, estado)
        self.direcao = direcao
        self.velocidade = velocidade
        
    def atribuiDirecao(self, direcao):
        self.direcao = direcao
            
    def atribuiVelocidade(self, velocidade):
        self.velocidade = velocidade
    
    def exibeEstado(self):
        print(super().exibeEstado())
        if(self.estado == 1):
            if(self.direcao == 1):
                return ('direcao: Horário\nvelocidade: %i' %(self.velocidade))
            elif(self.direcao == 0):
                return ('direcao: Anti-Horário\nvelocidade: %i' %(self.velocidade))
        else:
            return ''

x=Motor("nome", 1, 0, 200)

print(x.exibeEstado())
