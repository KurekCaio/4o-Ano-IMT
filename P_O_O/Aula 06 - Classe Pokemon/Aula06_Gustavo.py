class Pokemon:
#métodos
    def __init__(self, nome, ID, HP = None, AT = None,
                 DF = None, SP_AT = None, SP_DF = None, SP = None, 
                 golpes = []): 
        self.name = nome
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
        print("\n\nPokemon {0}:\nID: {1}\nHP: {2}\nAT: {3}\nDF: {4}\nSP_AT: {5}\nSP_DF: {6}\nSP: {7}\ngolpes: {8}\n\n"
    .format(self.name,self.ID,self.HP,self.AT,self.DF,self.SP_AT,self.SP_DF,self.SP,self.golpes))
        
        
pk1 = Pokemon("Charizard", 1)
pk1.atribuiHP(78)
pk1.atribuiAT(84)
pk1.atribuiDF(78)
pk1.atribuiSP_AT(109)
pk1.atribuiSP_DF(85)
pk1.atribuiSP(100)
pk1.aprendeGolpe('Garra de dragão')
pk1.aprendeGolpe('Rajada de fogo')

pk1.info()