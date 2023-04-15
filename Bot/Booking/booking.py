import os
from Booking.booking_filtration import BookingFiltration
import Booking.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium import webdriver



def block(self):
        try:
            close = self.find_element(By.CSS_SELECTOR,'button[aria-label="Dismiss sign-in info."]')
            close.click()
            close = self.find_element(By.CSS_SELECTOR,'path[d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"]')
            close.click()
            
        except:
            check = 1


class Booking(webdriver.Firefox):

    def __init__ (self,teardown):
    # def __init__ (self):

        self.teardown = teardown
        super(Booking, self).__init__()
        # self.implicitly_wait(30)
        self.maximize_window()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency = self.find_element(By.CLASS_NAME, 'e57ffa4eb5')
        currency.click()
        self.implicitly_wait(5)
        block(self)
        selected_currency = self.find_element(By.CLASS_NAME,'cf67405157')
        block(self)
        
        self.implicitly_wait(5)
        block(self)
        selected_currency.click()
        block(self)

    def selectPlaceToGo(self, placeToGo):
         search_field = self.find_element(By.ID, ':Ra9:')
         search_field.clear()
         search_field.send_keys(placeToGo)
         block(self)

    def selectDate(self, checkInDate, checkOutDate):
        field = self.find_element(By.CLASS_NAME,"b91c144835")
        block(self)

        field.click()
        # nextPage = self.find_element(By.CSS_SELECTOR,'button[class="fc63351294.a822bdf511.e3c025e003.fa565176a8.cfb238afa1.c334e6f658.ae1678b153.c9fa5fc96d.be298b15fa"]')
        # nextPage.click()
        # nextPage.click()


        # self.implicitly_wait(10)
        # try:
        #     close = self.find_element(By.CSS_SELECTOR,'btn[aria-label="Dismiss sign-in info."]')
        #     close.click()
        #     close = self.find_element(By.ID,'close')
        #     close.click()
        #     field.click()

        # except:
        #     field.click()
        #     field.click()
        
        checkInElement = self.find_element(By.CSS_SELECTOR, f'span[data-date="{checkInDate}"]')
        block(self)

        checkInElement.click()
        self.implicitly_wait(5)
        block(self)
        # field.click()


        # # try:
        # #     close = self.find_element(By.ID,'close')
        # #     close.click()

        # # except:
        # #     check = 1      
        # monthOne = int(checkInDate[5:7])
        # monthTwo = int(checkOutDate[5:7])
        # print(monthOne)
        # print(monthTwo)

        # yearOne = int(checkInDate[0:4])
        # yearTwo = int(checkOutDate[0:4])

        # if yearTwo>yearOne:
        #     monthTwo=monthTwo * (12*(yearTwo-yearOne))
        # if monthTwo-monthOne>1:
        #     print("Yes")
        #     block(self)

        #     rep = monthTwo-monthOne-1
        #     nextPage = self.find_element(By.CSS_SELECTOR,'path[d="M9.45 6c.2 0 .39.078.53.22l5 5c.208.206.323.487.32.78a1.1 1.1 0 0 1-.32.78l-5 5a.75.75 0 0 1-1.06 0 .74.74 0 0 1 0-1.06L13.64 12 8.92 7.28a.74.74 0 0 1 0-1.06.73.73 0 0 1 .53-.22zm4.47 5.72zm0 .57z"]')
        #     for i in range(rep):
        #         # block(self)
        #         nextPage.click()  



        # # try:
        # #     close = self.find_element(By.ID,'close')
        # #     close.click()

        # # except:
        # #     check = 1           
        # block(self)
        # field.click()
        
        checkOutElement = self.find_element(By.CSS_SELECTOR, f'span[data-date="{checkOutDate}"]')
        checkOutElement.click()

        #  firstResult = self.find_element(By.CSS_SELECTOR, "") //Cant get the first result
    
    def select_adults(self, count=1):
        block(self)
        self.implicitly_wait(3)
        block(self)
        self.implicitly_wait(5)
        block(self)
        adults = self.find_element(By.CLASS_NAME,"d67edddcf0")
        adults.click()

        while True:
            decrease = self.find_element(By.CSS_SELECTOR,'path[d="M20.25 12.75H3.75a.75.75 0 0 1 0-1.5h16.5a.75.75 0 0 1 0 1.5z"]')
            decrease.click()
            self.implicitly_wait(3)
            block(self)
            adultCountElement =self.find_element(By.ID,"group_adults")
            # self.implicitly_wait(3)
            block(self)
            adultCount = adultCountElement.get_attribute("value")
            # print(f'{adultCount} lalalal')
            if int(adultCount)==1:
                break
        # print(adultCount)

        increase = self.find_element(By.CSS_SELECTOR,'path[d="M20.25 11.25h-7.5v-7.5a.75.75 0 0 0-1.5 0v7.5h-7.5a.75.75 0 0 0 0 1.5h7.5v7.5a.75.75 0 0 0 1.5 0v-7.5h7.5a.75.75 0 0 0 0-1.5z"]')
        for i in range(count-1):
            increase.click()
        # self.implicitly_wait(2)
        # block(self)
    # def select_children(self, count=0):
    #     block(self)
    #     while True:
    #         childCountElement =self.find_element(By.ID,"group_children")
    #         # self.implicitly_wait(3)
    #         block(self)
    #         childCount = childCountElement.get_attribute("value")
    #         # print(f'{adultCount} lalalal')
    #         if int(childCount)==0:
    #             break
    #         decrease = self.find_element(By.CSS_SELECTOR,'path[d="M20.25 12.75H3.75a.75.75 0 0 1 0-1.5h16.5a.75.75 0 0 1 0 1.5z"]')
    #         decrease.click()
    #         self.implicitly_wait(3)
    #         block(self)

    #     # print(adultCount)

    #     increase = self.find_element(By.CSS_SELECTOR,'path[d="M20.25 11.25h-7.5v-7.5a.75.75 0 0 0-1.5 0v7.5h-7.5a.75.75 0 0 0 0 1.5h7.5v7.5a.75.75 0 0 0 1.5 0v-7.5h7.5a.75.75 0 0 0 0-1.5z"]')
    #     for i in range(count-1):
    #         increase.click()
    #     # self.implicitly_wait(2)
    #     # block(self)

    def submit(self):
        submit = self.find_element(By.CSS_SELECTOR,'Button[type="submit"]')
        submit.click()

    def apply_filtration(self):
        filter = BookingFiltration(driver=self)
        filter.sortPrice()
        self.implicitly_wait(100)
        filter.applyStarRating(4,5)