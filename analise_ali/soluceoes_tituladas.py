
'''
#peso molecular
pm = 98.08
#volume solucao em l ex 0.1 L se for fazer em ml Converta para litros
v = 100/1000
#Normalidae da solucao ex 0,5 N
N = 0.5
#numero de hidrogenios ionizaveis ex: 2
n = 2
#Calculo de massa da solucao
massa_obt = float((pm*v*N)/n)
print(f'A massa calculada foi de {massa_obt}g')
#Convertendo a solucao em litros:
densidade_solucao = 1.83
# calculo do volume da solucao:
solucao_em_volume = float(massa_obt/densidade_solucao)
print(f'O volume da sua solucao é {solucao_em_volume:,.3f}mL')
#pureza da solucao em %
pureza_solucao = 0.998
# correcao da pureza da solucao Ex: 1,34 * (100% ou 1)*(99.8% ou 0.998)
correcao_pureza = float(((solucao_em_volume*1)*pureza_solucao))
print(f'Voce deve adicionar {correcao_pureza:,.3f}mL para preparar sua solucao!')
'''
'''
while True:
    print('Bem vindo a calculadora de solucoes do Anil')
    calcular = input('O que voce deseja fazer? (V) ')
    
    if calcular == 'v':
        v = float(input('Insira o volume desejado, coloque em ml: '))
        if v < 1000:
            volume = v/1000
            print(f'O volume adicionado foi de {volume}L')
        elif v >= 1000:
            print(f'O volume a ser preparado é de {v}ml de solucao')
'''

class solucao:

    def __init__(self):
        #peso molecular
        self.pm = 98.08
        #volume solucao
        self.v = 0.1
        #Normalidae da solucao
        self.N = 0.5
        #numero de hidrogenios ionizaveis
        self.n = 2
        #massa da solucao
        self.m = 0
        #Densidade da solucao
        self.densidade = 1.83
        #Pureza da solucao
        self.pureza = 0.998
        
        
    

    def calculo_massa(self):
        self.m = float((self.pm*self.v*self.N)/self.n)
        #print(f'A massa da sua solucao é de {self.m}')
        return self.m
    def calculo_volume(self):
        self.calculo_volume = (self.calculo_massa()/self.densidade)
        #print(f'Voce deve adicionar {self.calculo_volume:.3f}ml')
        return self.calculo_volume
    def correcao_pureza(self):
        self.correcao_pureza = self.calculo_volume*1*self.pureza
        #print(self.correcao_pureza)
        return self.correcao_pureza
    
    #ma = massa molar da minha solucao titulante
    #va = volume utilizado da minha solucao titulante
    #vb = volume tutulado da solucao que eu desejo descobrir a molaridade

    def calculo_molar(self, ma, va, vb,):
        molaridade_meu_reagente = (ma*va)/vb
        print(molaridade_meu_reagente)
        return molaridade_meu_reagente
    
    # m's sao as molaridades achadas, ou os calculos molares 
    # q = quantidade de molaridades encontradas
    # mol_conhecida é a molaridade do reagente utilizada para titular a nossa solucao.
    
    def fator_correcao(self, m1, m2, m3, q='', mol_conhecida=''):
        fat_correct = ((m1+m2+m3)/(q*mol_conhecida))
        #print(fat_correct)
        return fat_correct
    
    # calcula a molaridade real de uma solucao. 
    def molaridade_real(self, molaridade_teorica):
        molaridade_real = self.fator_correcao(m1=0.502, m2=0.501, m3=0.502, q=3, mol_conhecida=0.5)*molaridade_teorica
        print(molaridade_real)
        return molaridade_real
    
def realiza_o_calculo():
    minha_funcao = solucao()
    print(f'{minha_funcao.calculo_massa():.3f}g')
    print(f'{minha_funcao.calculo_volume():.3f}ml')
    print(f'{minha_funcao.correcao_pureza():.3f}ml')

    minha_funcao.fator_correcao(m1=0.502, m2=0.501, m3=0.502, q=3, mol_conhecida=0.5)
    minha_funcao.calculo_molar(0.5, 25.2, 25)
    minha_funcao.molaridade_real(0.5)
realiza_o_calculo()














    
