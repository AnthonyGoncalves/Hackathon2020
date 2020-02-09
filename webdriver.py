from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller
import json
#import client_data

# Read in Json Info
client_data = json.load(open('client_data.json', 'r'))

def hitKey(key, amount):

    keyboard = Controller()
    if key == 'tab':
        for i in range(amount):
            keyboard.press('\t')
            keyboard.release('\t')
            sleep(.2)
    elif key == 'enter':
        for i in range(amount):
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            sleep(.2)
class GroupMeBot:

    def __init__(self):
        # Bot info
        self.email = 'hackbubot@gmail.com'
        self.password = 'password'
        self.driver = webdriver.Chrome()

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

    def addClientToGroup(self, phone_num, name, preference):
        try:
            # Client info
            self.num = phone_num
            self.name = name
            self.pref = preference

            # Click Search Bar for pref
            self.driver.find_element_by_xpath('/html/body/div[1]/aside/div[2]/div[2]/input').send_keys(self.pref)
            sleep(0.2)
            hitKey('tab', 2)
            sleep(1)
            hitKey('enter', 1)
            sleep(1)
            hitKey('tab', 17)
            hitKey('enter', 2)
            hitKey('tab', 4)
            hitKey('enter', 1)
            sleep(1)
            self.keyboard.type(self.num)
            sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[3]/div[2]/button').click()
            sleep(.5)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div[1]/div[1]/input').send_keys(self.name)
            # Add
            sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div[2]/button').click()
            sleep(1)
            # Add 1 member
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/button').click()
            sleep(.5)
            self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]/div')\
                .send_keys(f"Welcome to the {self.pref} Group, {self.name}! Introduce yourself to the Group! \n")
            sleep(.5)


        except Exception as e:
            print(f'[{self.name} IS NOT IN QUERY]', e)


my_bot = GroupMeBot()
my_bot.logIn()
my_bot.addClientToGroup(client_data[0], client_data[1], client_data[2])
