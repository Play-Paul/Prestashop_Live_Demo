from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Initialise webdriver
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()

#Call provided url
driver.get("https://demo.prestashop.com/#/en/front")
time.sleep(30)

#Select Item (Tshirt) and pick 100 quantity
driver.find_element(By.XPATH, "//*[@id='content']/section[1]/div/div[1]/article/div/div[1]/a/picture/img").click()
driver.find_element(By.XPATH, "//*[@id='quantity_wanted']").send_keys("100")
time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-or-refresh']/div[2]/div/div[2]/button").click()
time.sleep(10)
#Proceed to checkout
driver.find_element(By.XPATH, "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/div/a/i").click()
time.sleep(10)
#Note the calculation of goods, shipping and then proceed to checkout
driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div[2]/div/a")
#Fill personal info form
driver.find_element(By.XPATH, "//*[@id='field-id_gender-1']").click()
driver.find_element(By.XPATH, "//*[@id='field-firstname']").send_keys("Emeka")
driver.find_element(By.XPATH, "//*[@id='field-lastname']").send_keys("Paul")
driver.find_element(By.XPATH, "//*[@id='field-email']").send_keys("info.playpro@gmailcom")
driver.find_element(By.XPATH, "//*[@id='customer-form']/div/div[8]/div[1]/span/label/input").click()
driver.find_element(By.XPATH, "//*[@id='customer-form']/footer/button").click()

time.sleep(5)
driver.quit()