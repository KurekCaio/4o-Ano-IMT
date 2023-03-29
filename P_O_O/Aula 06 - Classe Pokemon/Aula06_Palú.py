class Pokemon:
#métodos
    def __init__(self, Nome = "", ID = 0, HP = 0, AT = 0, DF = 0, SP_AT = 0, SP_DF = 0, SP = 0, Golpes = []):
        self._Nome = Nome
        self._ID = ID
        self._HP = HP
        self._AT = AT
        self._DF = DF
        self._SP_AT = SP_AT
        self._SP_DF = SP_DF
        self._SP = SP
        self._Golpes = Golpes
        
    def atribuiNome(self, Nome):
        self._Nome = Nome
        
    def atribuiID(self, ID):
        self._ID = ID
        
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
        
    def atribuiGolpes(self, Golpes):
        self._Golpes.append(Golpes)
        
    def info(self):
        """self.__dict__"""
        print("\nPokemon {0}:\nID: {1}\nHP: {2}\nAT: {3}\nDF: {4}\nSP_AT: {5}\nSP_DF: {6}\nSP: {7}\nGolpes: {8}".format(self._Nome,self._ID,self._HP,self._AT,self._DF,self._SP_AT,self._SP_DF,self._SP,self._Golpes))

n = 0
i = 0

print("\n\nBEM VINDO AO CADASTRO DE POKEMONS\nOBS: Os Pokemons Charizard e Rapidash estão criados no final do código\n\n")

i = int(input("Quantos Pokemons deseja cadastrar?\n"))      

lista_de_pokemon = {}

while n < i:
    
    v = 0
    
    poke = Pokemon()
    poke.atribuiNome(input("\nDigite o nome do Pokemon %i:\n"%(n+1)))
    poke.atribuiID(int(input("\nDigite o ID do(a) {0}:\n".format(poke._Nome))))
    poke.atribuiHP(int(input("\nDigite o HP do(a) {0}:\n".format(poke._Nome))))
    poke.atribuiAT(int(input("\nDigite o AT do(a) {0}:\n".format(poke._Nome))))
    poke.atribuiDF(int(input("\nDigite a defesa do(a) {0}:\n".format(poke._Nome))))
    poke.atribuiSP_AT(int(input("\nDigite a velocidade de ataque do(a) {0}:\n".format(poke._Nome))))
    poke.atribuiSP_DF(int(input("\nDigite a velocidade de defesa do(a) {0}:\n".format(poke._Nome))))
    poke.atribuiSP(int(input("\nDigite a velocidade do(a) {0}:\n".format(poke._Nome))))
    
    n_golpes = (int(input("\nQuantos golpes esse Pokemon terá?\n")))
    
    poke._Golpes.clear()
    
    while v < n_golpes:
        poke.atribuiGolpes(input("\nDigite o nome do golpe %i do Pokemon:\n"%(v+1)))
        v+=1

    lista_de_pokemon[poke._ID] = poke
    n+=1
    
    poke.info()
    
Charizard = Pokemon()
Charizard._Golpes.clear()
Charizard.atribuiNome("Charizard")
Charizard.atribuiID(450)
Charizard.atribuiHP(55)
Charizard.atribuiAT(99)
Charizard.atribuiDF(50)
Charizard.atribuiSP_AT(60)
Charizard.atribuiSP_DF(75)
Charizard.atribuiSP(10)
Charizard.atribuiGolpes("Bola de Fogo")
Charizard.atribuiGolpes("Chama")
Charizard.info()

Rapidash = Pokemon()
Charizard._Golpes.clear()
Rapidash.atribuiNome("Rapidash")
Rapidash.atribuiID(300)
Rapidash.atribuiHP(30)
Rapidash.atribuiAT(99)
Rapidash.atribuiDF(20)
Rapidash.atribuiSP_AT(99)
Rapidash.atribuiSP_DF(99)
Rapidash.atribuiSP(99)
Rapidash.atribuiGolpes("Coice")
Rapidash.atribuiGolpes("Cabeçada Flamejante")
Rapidash.info()
    
