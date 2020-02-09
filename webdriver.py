from selenium import webdriver
from time import sleep
import questionscript

class GroupMeBot:

    def __init__(self):

        self.email = 'hackbubot@gmail.com'
        self.password = 'password'
        self.driver = webdriver.Chrome()

    def logIn(self):
        try:
            # Go to GroupMe.com!
            self.driver.get('https://groupme.com')
            sleep(1)

            # Clicks Log in
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/p/a').click()
            sleep(1)

            # Enters email and password, then clicks Log in!
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/form/div[1]/input").send_keys(self.email)
            self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/form/div[2]/input').send_keys(self.password)
            self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/form/button').click()

            sleep(100)
        except Exception as e:
            print('[EXCEPTION]', e)

    def addClient(self):
        pass

    def addToGroup(self):
        pass

my_bot = GroupMeBot()
my_bot.logIn()