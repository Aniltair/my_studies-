from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class scielo:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.scielo.br/'
    def navigate(self):
        self.driver.get(self.url) 
def pesquisar_pg_inicial():
    def clicar_pg_init():
        clk = ff.find_element(By.CSS_SELECTOR, ('input.btn')).click()
        return clk
    bar =  ff.find_element(By.NAME, 'q[]')
    pesquisar =  bar.send_keys('food')#input('O que deseja pesquisar? '))
    time.sleep(1)
    clicar_pg_init()
    return pesquisar
def pagina():
    time.sleep(1)
    # idioma =  ff.find_element(By.CSS_SELECTOR, '#in_scl').click()
    visualizacao = ff.find_element(By.CSS_SELECTOR, "#ul_journal_title > li:nth-child(11) > div:nth-child(1) > label:nth-child(2)")
    ff.execute_script("arguments[0].scrollIntoView();", visualizacao)
    time.sleep(3)
    idioma = ff.find_element(By.CSS_SELECTOR, '#ul_la > li:nth-child(2) > div:nth-child(1) > label:nth-child(2)').click() #seleciona o idioma portugues
    filtrar = ff.find_element(By.CSS_SELECTOR, '#apply_filters_button').click() #filtra
    time.sleep(1)
#ff.quit() fecha o navegador

ff = webdriver.Firefox()
g = scielo(ff)
g.navigate()
pesquisar_pg_inicial()
pagina()







