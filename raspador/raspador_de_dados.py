from selenium import webdriver
from selenium.webdriver.common.by import By


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
    def navigate(self):
        self.driver.get(self.url) 

ff = webdriver.Firefox()
g = Google(ff)
g.navigate()
bar =  ff.find_element(By.CLASS_NAME, "gLFyf")
bar.send_keys('youtube') #bar.send_keys(input('O que deseja pesquisar?'))



