import os
import Booking.constants as const
from selenium import webdriver


class Booking(webdriver.Firefox):
    # def __init__ (self,teardown):
    def __init__ (self):

        # self.teardown = teardown
        super(Booking, self).__init__()
    def __exit__(self, exc_type, exc_val, exc_tb):
        # if self.teardown:
            self.quit()
    def land_first_page(self):
        self.get(const.BASE_URL)