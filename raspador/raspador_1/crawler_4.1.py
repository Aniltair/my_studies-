from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#import requests as r
#from bs4 import BeautifulSoup

class scielo:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://bdtd.ibict.br/vufind/'
        self.pesquisa = '#searchForm_lookfor' #bara de pesquisa inicial 
        self.botao_pesquisa_1 = 'button.btn'  #Botao de pesquisa da barra inicial
        self.ver_mais = '//*[@id="detail"]' #xpath
        self.informacoes =  'div.col-sm-12:nth-child(1)' #todas as informacoes da aba
        # informacoes dos artigos  
        self.titulo = 'div.col-sm-12:nth-child(1) > h3:nth-child(1)' #Css selector
        self.resumo = 'div.col-sm-12:nth-child(1) > p:nth-child(2)' #Css selector
        self.data_defesa = 'table.table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(2)'
        self.autor = 'table.table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(2)'
        self.tipo_documento = 'table.table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(4)'
        self.idioma = 'table.table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(5)'
        self.assunto = 'table.table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(6)'
        self.texto_completo = 'table.table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(7)'
        self.descricao = 'table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1)'
        self.ano_de = '#publishDatefrom'
        self.ano_ate = '#publishDateto'
        self.clicavel = 'input.btn'
    #inicia o driver
    def navigate(self):
        self.driver.get(self.url)
    # funcao que clica em objetos
    def clicar(botao):
        clk = driver.find_element(By.CSS_SELECTOR, botao).click() #o valor de botao retorna o que eu quero clicar acima.
        return clk 
    #Pesquisa na barra da página
    def pesquisar(self):
        scielo.clicar(self.pesquisa) #estou clicando no botao de busca
        barra = driver.find_element(By.CSS_SELECTOR, '#searchForm_lookfor')
        pesquisar = barra.send_keys(input('O que voce gostaria de pesquisar? ')) # essa e a barra de pesquisa
        time.sleep(1)
        scielo.clicar(self.botao_pesquisa_1)# isso clica no pesquisar
        return pesquisar
    #pega o botao ver+
    def get_botao(self):
        bota = driver.find_elements(By.XPATH, self.ver_mais)
    #objetos da página
    def titulo_1(self):
            titulo_1 = driver.find_element(By.CSS_SELECTOR, self.titulo).text
            print(' ')
            return print(f'# {titulo_1}')
    def resumo_1(self):  
        resumo_1 = driver.find_element(By.CSS_SELECTOR, self.resumo).text
        print(' ')
        return print(f'{resumo_1}')
    def data_defesa_1(self):
            data_defesa_1 = driver.find_element(By.CSS_SELECTOR, self.data_defesa).text
            print(' ')
            return print(f'{data_defesa_1}')
    def autor_1(self):
            autor_1 = driver.find_element(By.CSS_SELECTOR, self.autor).text   
            return print(f'#{autor_1}')
    def tipo_doc_1(self):
            tipo_documento_1 = driver.find_element(By.CSS_SELECTOR, self.tipo_documento).text
            print(' ')
            return print(f'{tipo_documento_1}')
    def idioma_1(self):
            idioma_1 = driver.find_element(By.CSS_SELECTOR, self.idioma).text
            print(' ')
            return print(f'{idioma_1}')
    def assunto_1(self):
            assunto_1 = driver.find_element(By.CSS_SELECTOR, self.assunto).text
            assunto_1= assunto_1.split(' ')
            print(' ')
            return print(f'#{assunto_1}')
    def texto_completo_1(self):
            texto_completo_1 = driver.find_element(By.CSS_SELECTOR, self.texto_completo).text
            print(' ')
            return print(f'{texto_completo_1}')
    def descricao_1(self):
            descricao_1 = driver.find_element(By.CSS_SELECTOR, self.descricao).text
            print(' ')
            return print(f'{descricao_1}')
    # ajusta as datas da pesquisa
    def de_(self):
        scielo.clicar(self.ano_de)
        ano1 = driver.find_element(By.CSS_SELECTOR, '#publishDatefrom')
        ano_pesquisa = ano1.send_keys(input('De: '))
        return ano_pesquisa
    def ate_(self):
        scielo.clicar(self.ano_ate)
        ano_1 = driver.find_element(By.CSS_SELECTOR, '#publishDateto')
        ano_pesquisa_1 = ano_1.send_keys(input('Até: '))
        return ano_pesquisa_1
    ''' # printa todo o conteudo da pagina
    def infos(self):
        infos = driver.find_element(By.CSS_SELECTOR, self.informacoes)
        print(infos.text)
        print('****************************************************')
        time.sleep(1)
    '''
    def definir(self):
       return driver.find_element(By.CSS_SELECTOR, 'input.btn').click()
    def copia(self):
        butons = driver.find_elements(By.CLASS_NAME, 'detail')
        for i in range(len(butons)):
            butons = driver.find_elements(By.CLASS_NAME, 'detail')
            butons[i].click()
            print('***********************************************')
            self.titulo_1()
            self.resumo_1()
            self.data_defesa_1()
            self.autor_1()
            self.tipo_doc_1()
            self.idioma_1()
            self.assunto_1()
            self.texto_completo_1()
            self.descricao_1()
            print('***********************************************')
            driver.execute_script("window.history.go(-1)")
            butons = driver.find_elements(By.CLASS_NAME, 'detail')
            time.sleep(4)
''' Requisita o html da pagina atual 
class requisicao:
    def __init__(self):
        self.url_atual = bdtd.driver.current_url
        self.response = r.get(self.url_atual)
    def atual_url(self):
        return  self.url_atual
'''

driver = webdriver.Firefox()
bdtd = scielo(driver)
bdtd.navigate()
bdtd.pesquisar()
bdtd.de_()
bdtd.ate_()
bdtd.definir()
bdtd.copia()

