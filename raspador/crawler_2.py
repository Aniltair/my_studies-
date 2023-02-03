from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class scielo:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.scielo.br/'
        self.item = 'item'
        self.titulo = '#ResultArea .title' #class
        self.autores = 'line authors' #class
        self.fonte = 'line source' #class
        self.resumo = 'abstract' #class
    def navigate(self):
        self.driver.get(self.url) 

    def _get_item(self):
        return self.driver.find_elements(By.CLASS_NAME, self.item)
 

    def _get_title(self, title):
       return ff.find_element(By.CSS_SELECTOR, self.titulo)
    
    def get_all_data(self):
        item = self._get_item()
        for items in item:
            print(self._get_title(items).text)
def pesquisar_pg_inicial():
    def clicar_pg_init():
        clk = ff.find_element(By.CSS_SELECTOR, ('input.btn')).click()
        return clk
    bar =  ff.find_element(By.NAME, 'q[]')
    pesquisar =  bar.send_keys('food')#input('O que deseja pesquisar? '))
    time.sleep(1)
    clicar_pg_init()
    return pesquisar

ff = webdriver.Firefox()
g = scielo(ff)
g.navigate()
pesquisar_pg_inicial()
g.get_all_data()
