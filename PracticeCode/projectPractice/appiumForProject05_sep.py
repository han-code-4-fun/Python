

from appium import webdriver
from time import sleep

#trigger=False
 
class Action():
    def __init__(self):

        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": ".main.MainActivity",
            'noReset': True,
            'newCommandTimeout': 0
        }

        self.server = 'http://localhost:4723/wd/hub'

        self.driver = webdriver.Remote(self.server, self.desired_caps)

        self.start_x = 600
        self.start_y = 1200
        self.distance = 1000
        #self.x = driver.get_window_size()['width']
        #self.y = driver.get_window_size()['height']

    def comments(self):
        sleep(2)

        self.driver.tap([(500, 1200)], 500)
    def getSleep(self):
        sleep(2)

    def reRoll(self):

        self.driver.swipe(self.start_x, self.start_y, self.start_x,
                          self.start_y - self.distance)
        sleep(2)

        self.driver.swipe(self.start_x, self.start_y, self.start_x,
                          self.start_y + self.distance)
 
    def scroll(self):
        #global trigger
        sleep(1)

        self.driver.swipe(self.start_x, self.start_y, self.start_x,
                              self.start_y-self.distance)
        #while True:
         #   sleep(45)
          #  self.driver.swipe(self.start_x, self.start_y, self.start_x,
           #                   self.start_y-self.distance)

        #self.driver.swipe(1/2*self.x, 3/7*self.y, 1/2*self.x, 6/7*self.y, 200)

            #trigger = False
        #sleep(2)
 
    #def main(self):
       # self.comments()
     #   self.scroll()
 
 
if __name__ == 'appiumForProject':
    sleep(1)
    action = Action()

