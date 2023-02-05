from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
    def navigate(self):
        self.driver.get(self.url) 
def pesquisar():
    bar =  ff.find_element(By.CLASS_NAME, "gLFyf")
    pesquisa =  bar.send_keys(input('O que deseja pesquisar? '))
    time.sleep(1)
    clicar()
    return pesquisa
def pesquisa_com_sorte():
    bar =  ff.find_element(By.CLASS_NAME, "gLFyf")
    pesquisa =  bar.send_keys(input('O que deseja pesquisar? '))
    time.sleep(1)
    clicar_sorte()
    return pesquisa_com_sorte
def clicar():
    clk = ff.find_element(By.CLASS_NAME, 'gNO89b').click()
    return clk
def clicar_sorte():
    clk_sorte = ff.find_element(By.CLASS_NAME, 'RNmpXc').click()
    return clk_sorte

#ff.quit() fecha o navegador

ff = webdriver.Firefox()
g = Google(ff)
g.navigate()







