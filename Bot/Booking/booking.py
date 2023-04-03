import os
import Booking.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class Booking(webdriver.Firefox):
    def __init__ (self,teardown):
    # def __init__ (self):

        self.teardown = teardown
        super(Booking, self).__init__()
        # self.implicitly_wait(15)
        self.maximize_window()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency = self.find_element(By.CLASS_NAME, 'e57ffa4eb5')
        currency.click()
        selected_currency = self.find_element(By.CLASS_NAME,'cf67405157')
        selected_currency.click()

    def selectPlaceToGo(self, placeToGo):
         search_field = self.find_element(By.ID, ':Ra9:')
         search_field.clear()
         search_field.send_keys(placeToGo)