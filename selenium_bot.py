import time

from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome(executable_path=r'chromedriver.exe')
navegador.get("https://login.live.com/")

navegador.find_element(By.NAME,'loginfmt').send_keys('digite seu email')
navegador.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()

time.sleep(1)

navegador.find_element(By.XPATH,'//*[@id="i0118"]').send_keys('digite sua senha')
navegador.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()

time.sleep(1)

navegador.find_element(By.XPATH,'//*[@id="KmsiCheckboxField"]').click()
navegador.find_element(By.XPATH,'//*[@id="idBtn_Back"]').click()

time.sleep(2)

navegador.find_element(By.XPATH,'//*[@id="home.cards.card.outlook.cold"]/div[1]/div[1]/span/span').click()




#senha_incorreta = navegador.find_element(By.XPATH,'//*[@id="idA_PWD_ForgotPassword"]').get_attribute("href")





time.sleep(1000)