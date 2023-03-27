class Pokemon:
    def __init__(self, nome, ID, HP = None, AT = None,
                 DF = None, SP_AT = None, SP_DF = None, SP = None, 
                 golpes = []):
        
        self._name = nome
        self._ID = ID
        self._HP = HP
        self._AT = AT
        self._DF = DF
        self._SP_AT = SP_AT
        self._SP_DF = SP_DF
        self._SP = SP
        self._golpes = golpes
      
    def atribuiHP(self, HP):
        self._HP = HP
        
    def atribuiAT(self, AT):
        self._AT = AT
        
    def atribuiDF(self, DF):
        self._DF = DF
        
    def atribuiSP_AT(self, SP_AT):
        self._SP_AT = SP_AT
        
    def atribuiSP_DF(self, SP_DF):
        self._SP_DF = SP_DF
        
    def atribuiSP(self, SP):
        self._SP = SP
        
    def aprendeGolpe(self, golpe):
        self._golpes.append(golpe)
        
    def info(self):
        print(f"\n\nPokemon {self._name}:\n\nID: {self._ID}\nHP: {self._HP}\nAT: {self._AT}\nDF: {self._DF}\nSP_AT: {self._SP_AT}\nSP_DF: {self._SP_DF}\nSP: {self._SP}\ngolpes: {self._golpes}\n\n")
        
        
pk1 = Pokemon("BLASTOISE", 3)
pk1.atribuiHP(90)
pk1.atribuiAT(70)
pk1.atribuiDF(85)
pk1.atribuiSP_AT(60)
pk1.atribuiSP_DF(75)
pk1.atribuiSP(65)
pk1.aprendeGolpe('Mordida')
pk1.aprendeGolpe('Raio Congelante')
pk1.aprendeGolpe('Canhão de Flash')

pk1.info()
