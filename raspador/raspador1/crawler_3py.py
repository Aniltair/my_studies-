from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class scielo:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://bdtd.ibict.br/vufind/'
        self.pesquisa = '#searchForm_lookfor' #bara de pesquisa inicial 
        self.botao_pesquisa_1 = 'button.btn'  #Botao de pesquisa da barra inicial 
        self.ver_mais = '#result1 > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(11) > div:nth-child(2) > a:nth-child(1)' # css
        self.inf = 'div.col-sm-12:nth-child(1)'
        self.box = 'result' #class
    def navigate(self):
        self.driver.get(self.url) 
    
    def clicar(botao):
        clk = drive.find_element(By.CSS_SELECTOR, botao).click() #o valor de botao retorna o que eu quero clicar acima.
        return clk 
    
    def pesquisar(self):
        scielo.clicar(self.pesquisa) #estou clicando no botao de busca
        barra = drive.find_element(By.CSS_SELECTOR, '#searchForm_lookfor')
        pesquisar = barra.send_keys('Food') # essa e a barra de pesquisa
        time.sleep(1)
        scielo.clicar(self.botao_pesquisa_1)# isso clica no pesquisar
        return pesquisar
    
    def ver(self):
        ver = scielo.clicar(self.ver_mais)
        return ver

    def infos(self):
        infos = drive.find_element(By.CSS_SELECTOR, self.inf)
        time.sleep(1)
        print(infos.text)
    
    def voltar(self):
        drive.back()
    
        
    def _get_boxes(self):
         caixas = drive.find_elements(By.CLASS_NAME, self.box )
         return caixas
    def get_all_data(self):
        boxes = self._get_boxes()
        for box in boxes:
            print(box.text)
drive = webdriver.Firefox()
bdtd = scielo(drive)
bdtd.navigate()
bdtd.pesquisar()
bdtd.get_all_data()
bdtd.ver()
bdtd.infos()
time.sleep(5)
bdtd.voltar()



