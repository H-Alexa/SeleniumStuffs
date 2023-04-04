#https://www.youtube.com/watch?v=j7VZsCCnptM


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#GETTING STARTED

driver = webdriver.Firefox();
# driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

# driver.implicitly_wait(5)
# myElement = driver.find_element(By.ID, 'downloadButton')

#IMPLICIT VS EXPLICIT
# myElement.click()

# progressElement = driver.find_element(By.CLASS_NAME, 'progress-label')
# print(f"{progressElement.text}") 
# print(f"{progressElement.text == 'Complete!'}")

# WebDriverWait(driver,30).until(
#     EC.text_to_be_present_in_element(
#         #element filtration
#         (By.CLASS_NAME, 'progress-label'),
#         #expected text
#         'Complete!'
#     )
# )

# progressElement = driver.find_element(By.CLASS_NAME, 'progress-label')
# print(f"{progressElement.text == 'Complete!'}")

#SENDING KEYS AND CSS SELECTORS

driver.get('https://byjus.com/addition-calculator/')
driver.implicitly_wait(5)
x = driver.find_element(By.ID,'x')
y = driver.find_element(By.ID,'y')

x.send_keys(Keys.NUMPAD1, Keys.NUMPAD2)
y.send_keys(13)

calculate = driver.find_element(By.CLASS_NAME, 'clcbtn')
calculate.click();
driver.implicitly_wait(20)
try:
    close = driver.find_element(By.CLASS_NAME,'close')
    close.click()
except: 
    print("All clear")