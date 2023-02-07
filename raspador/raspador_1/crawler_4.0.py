from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests as r
from bs4 import BeautifulSoup

class scielo:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://bdtd.ibict.br/vufind/'
        self.pesquisa = '#searchForm_lookfor' #bara de pesquisa inicial 
        self.botao_pesquisa_1 = 'button.btn'  #Botao de pesquisa da barra inicial
        self.ver_mais = '//*[@id="detail"]' #xpath
        self.informacoes =  'div.col-sm-12:nth-child(1)'  
    def navigate(self):
        self.driver.get(self.url)

    def clicar(botao):
        clk = driver.find_element(By.CSS_SELECTOR, botao).click() #o valor de botao retorna o que eu quero clicar acima.
        return clk 
    
    def pesquisar(self):
        scielo.clicar(self.pesquisa) #estou clicando no botao de busca
        barra = driver.find_element(By.CSS_SELECTOR, '#searchForm_lookfor')
        pesquisar = barra.send_keys('Food') # essa e a barra de pesquisa
        time.sleep(1)
        scielo.clicar(self.botao_pesquisa_1)# isso clica no pesquisar
        return pesquisar
    
    def ver(self):
        ver = scielo.clicar(self.ver_mais)
        return ver
    
    def get_botao(self):
        bota = driver.find_elements(By.XPATH, self.ver_mais)
        
    
    def voltar(self):
        driver.back()

    def infos(self):
        infos = driver.find_element(By.CSS_SELECTOR, self.informacoes)
        print(infos.text)
        print('****************************************************')
        time.sleep(1)
    
    def get_all_botao(self):
        butons = driver.find_elements(By.CLASS_NAME, 'detail')
        for i in range(len(butons)):
            butons = driver.find_elements(By.CLASS_NAME, 'detail')
            butons[i].click()
            self.infos()
            driver.execute_script("window.history.go(-1)")
            butons = driver.find_elements(By.CLASS_NAME, 'detail')
            time.sleep(2)

# class requisicao:
#     def __init__(self):
#         self.url_atual = bdtd.driver.current_url
#         self.response = r.get(self.url_atual)
#     def atual_url(self):
#         return  self.url_atual




driver = webdriver.Firefox()
bdtd = scielo(driver)
bdtd.navigate()
bdtd.pesquisar()
bdtd.get_all_botao()
#req = requisicao() #para chamar algum argumento da requisicao, eu devo retornar com req.argumento
