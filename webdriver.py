from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller
import questionscript
#import client_data




class GroupMeBot:

    def __init__(self ):
        # Bot info
        self.email = 'hackbubot@gmail.com'
        self.password = 'password'
        self.driver = webdriver.Chrome()

        # Client info
        self.name = 'Anthony'
        self.phone_number = '9148605694'
        self.pref = 'Video Games'

        # Bot Input
        self.keyboard = Controller()


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

            sleep(1)


        except Exception as e:
            print('[EXCEPTION]', e)

    def addClientToGroup(self):

        # Click Search Bar for pref
        self.driver.find_element_by_xpath('/html/body/div[1]/aside/div[2]/div[2]/input').send_keys(self.pref)
        sleep(0.2)
        for i in range(2):
            self.keyboard.press('\t')
            self.keyboard.release('\t')
        sleep(1)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        sleep(1)
        for i in range(17):
            self.keyboard.press('\t')
            self.keyboard.release('\t')
            sleep(.2)
        for i in range(2):
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)
        for i in range(4):
            self.keyboard.press('\t')
            self.keyboard.release('\t')
            sleep(.5)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        sleep(1)
        self.keyboard.type(self.phone_number)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[3]/div[2]/button').click()
        sleep(.5)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div[1]/div[1]/input').send_keys(self.name)
        '''for i in range(2):
            self.keyboard.press('\t')
            self.keyboard.release('\t')
            sleep(.2)'''
        # Add
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div[2]/button').click()
        sleep(1)
        # Add 1 member
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/button').click()

        sleep(.5)

my_bot = GroupMeBot()
my_bot.logIn()
my_bot.addClientToGroup()
