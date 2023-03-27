class Pokemon:
#métodos
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
        
    '''
    def atribuiNome(self, nome):
        self._name = nome
        
    def atribuiID(self, ID):
        self._ID = ID
    '''
      
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
        print("\n\nPokemon {0}:\nID: {1}\nHP: {2}\nAT: {3}\nDF: {4}\nSP_AT: {5}\nSP_DF: {6}\nSP: {7}\ngolpes: {8}\n\n"
    .format(self._name,self._ID,self._HP,self._AT,self._DF,self._SP_AT,self._SP_DF,self._SP,self._golpes))
        
        
pk1 = Pokemon("PIKACHU", 9)
pk1.atribuiHP(14)
pk1.atribuiAT(8)
pk1.atribuiDF(3)
pk1.atribuiSP_AT(10)
pk1.atribuiSP_DF(7)
pk1.atribuiSP(6)
pk1.aprendeGolpe('Hadouken')

pk1.aprendeGolpe('Shoryuken')
pk1.atribuiSP_AT(5)

pk1.info()
