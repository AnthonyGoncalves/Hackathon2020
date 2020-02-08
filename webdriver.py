from selenium import webdriver
from time import sleep

class GroupMeBot:

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.get('https://groupme.com')
        sleep(10)

GroupMeBot()