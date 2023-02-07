from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests as r
from bs4 import BeautifulSoup


class raspador:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://scholar.google.com.br'
        self.bloco = 'div.gs_or:nth-child(1)'
        self.titulo = 'div.gs_or:nth-child(1) > div:nth-child(1) > h3:nth-child(1)'
        self.referencia = 'div.gs_or:nth-child(1) > div:nth-child(1) > div:nth-child(2)'
        self.resumo = 'div.gs_or:nth-child(1) > div:nth-child(1) > div:nth-child(3)'
        





    def navegar(self):
        #self.driver.get(f'http://{self.url}.com') um exemplo de como pode ser requisitada uma url. 
        self.driver.get(self.url)
    def clk(self, par_):
        return driver.find_element(By.CSS_SELECTOR, par_).click()   
    def encontra_elemento_css(self, elemento_):
        return driver.find_element(By.CSS_SELECTOR, elemento_)
    def barra_pesquisa(self):
        barra = self.encontra_elemento_css('#gs_hdr_tsi')
        pq = barra.send_keys('alimento')
        return self.clk('#gs_hdr_tsb')
    def voltar(self):
      return driver.execute_script("window.history.go(-1)")
    def periodo(self):   
        self.clk('#gs_res_sb_yyc')
        de = self.encontra_elemento_css('#gs_as_ylo')
        ate = self.encontra_elemento_css('div.gs_res_sb_yyr:nth-child(4) > div:nth-child(2) > input:nth-child(1)')
        de_ = de.send_keys(input('De: '))
        ate_ = ate.send_keys(input('Até: '))
        return self.clk('div.gs_res_sb_yyr:nth-child(5) > button:nth-child(1)')
    def ordernar_data(self):
        self.clk('ul.gs_bdy_sb_sec:nth-child(2) > li:nth-child(2) > a:nth-child(1)')
    def ordenar_relevancia(self):
        self.clk('ul.gs_bdy_sb_sec:nth-child(2) > li:nth-child(1) > a:nth-child(1)')
    def qualquer_tipo(self):
        self.clk('ul.gs_bdy_sb_sec:nth-child(4) > li:nth-child(1) > a:nth-child(1)')
    def artigo_revisao(self):
        self.clk('ul.gs_bdy_sb_sec:nth-child(4) > li:nth-child(2) > a:nth-child(1)')

    def O_artigo(self):
        artigos = driver.find_elements(By.CLASS_NAME, 'div.gs_or:nth-child(1)')
        for i in range(len(artigos)):
            att = driver.find_elements(By.CLASS_NAME, 'div.gs_or:nth-child(1)')
            print(att.tex[i])
            artigos = driver.find_elements(By.CLASS_NAME, 'div.gs_or:nth-child(1)')
# ctrl k + c para comentar o codigo
# ctrl l + u para descomentar o que esta comentado

driver = webdriver.Firefox()
raspador = raspador(driver)
raspador.navegar()
raspador.barra_pesquisa()
#raspador.periodo()
raspador.ordernar_data()
raspador.O_artigo()






        