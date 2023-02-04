from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests as r
from bs4 import BeautifulSoup as bs

class scielo:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.scielo.br/'
        self.pesquisa = 'div.form-textarea:nth-child(1) > textarea:nth-child(1)' #bara de pesquisa inicial
        self.botao = 'html.no-js body.collection section.levelMenu div.container form.searchForm.searchFormBuilder div.col-md-2.col-sm-2 input.btn.btn-primary.glyph.glyph-search'
    def navigate(self):
        self.driver.get(self.url)

    def clicar(botao):
        clk = driver.find_element(By.CSS_SELECTOR, botao).click() #o valor de botao retorna o que eu quero clicar acima.
        return clk 
    
    def pesquisar(self):
        scielo.clicar(self.pesquisa) #estou clicando no botao de busca
        barra = driver.find_element(By.CSS_SELECTOR, 'div.form-textarea:nth-child(1) > textarea:nth-child(1)')
        pesquisar = barra.send_keys('Food') # essa e a barra de pesquisa
        time.sleep(1)
        scielo.clicar(self.botao)# isso clica no pesquisar
        return pesquisar
    
    def ver(self):
        ver = scielo.clicar(self.ver_mais)
        return ver
    
    
    def voltar(self):
        driver.back()


class requisicao:
    def __init__(self):
        self.url_atual = bdtd.driver.current_url
        self.response = r.get(self.url_atual)
    def atual_url(self):
        return  self.url_atual

class sopa:
    def __init__(self):
        self.url = requisicao.atual_url
        self.site = bs(self.url, 'html.parser')
        self.botoes = self.site.find_all('')
    pass
        



driver = webdriver.Firefox()
bdtd = scielo(driver)
bdtd.navigate()
bdtd.pesquisar()

