class Pokemon:
#métodos
    def __init__(self, 
                 nome, 
                 ID, 
                 HP = None, 
                 AT = None,
                 DF = None, 
                 SP_AT = None, 
                 SP_DF = None, 
                 SP = None, 
                 golpes = []):
        
        self.nome = nome
        self.ID = ID
        self.HP = HP
        self.AT = AT
        self.DF = DF
        self.SP_AT = SP_AT
        self.SP_DF = SP_DF
        self.SP = SP
        self.golpes = golpes  
        
    def atribuiHP(self, HP):
        self.HP = HP
        
    def atribuiAT(self, AT):
        self.AT = AT
        
    def atribuiDF(self, DF):
        self.DF = DF
        
    def atribuiSP_AT(self, SP_AT):
        self.SP_AT = SP_AT
        
    def atribuiSP_DF(self, SP_DF):
        self.SP_DF = SP_DF
        
    def atribuiSP(self, SP):
        self.SP = SP
        
    def aprendeGolpe(self, golpe):
        self.golpes.append(golpe)

    def info(self):
        print("\n==========\n Pokemon: {0}\n ID: {1}\n HP: {2}\n AT: {3}\n DF: {4}\n SP_AT: {5}\n SP_DF: {6}\n SP: {7}\n Golpes: {8}\n=========="
              .format(self.nome,self.ID,self.HP,self.AT,self.DF,self.SP_AT,self.SP_DF,self.SP,self.golpes))
        
Tirica = Pokemon("Tiririca",2222)
Tirica.atribuiHP(55)
Tirica.atribuiAT(1)
Tirica.atribuiDF(-10)
Tirica.atribuiSP_AT(20)
Tirica.atribuiSP_DF(5)
Tirica.atribuiSP(100)
Tirica.aprendeGolpe("Buzina supersonica")
Tirica.aprendeGolpe("Gas do riso")
Tirica.info()
