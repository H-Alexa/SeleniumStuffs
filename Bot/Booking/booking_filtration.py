
#filtering results
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BookingFiltration():
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def applyStarRating(self, *starValues):
        self.driver.implicitly_wait(200)
        starBox = self.driver.find_element(By.ID,"filter_group_class_:R14q:")
        starChild = starBox.find_elements(By.CSS_SELECTOR,"*")
        for starValue in starValues:

            for starElement in starChild:
                if str(starElement.get_attribute('innerHTML')).strip() == f'{starValue} stars':
                    starElement.click()

        self.driver.implicitly_wait(200)
        
    
    def sortPrice(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element(By.CSS_SELECTOR,'Button[data-selected-sorter="popularity"')
        element.click()

        self.driver.implicitly_wait(200)

        priceElement = self.driver.find_element(By.CLASS_NAME,"ff0ad2a91a")
        priceElements = priceElement.find_elements(By.CSS_SELECTOR,"*")
        for price in priceElements:
            try:
                if str(price.get_attribute('innerHTML')).strip() == "Price (lowest first)":
                    try:
                        price.click()
                    except:
                        check = 1
            except:
                check = 1