from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class MainPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super(MainPage, self).__init__(driver)
        self.__cookieClikerlocator = (By.ID, "tooltipAnchor")


