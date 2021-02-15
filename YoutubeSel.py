from selenium import webdriver

class music(): #class knowm as info
    def __init__(self):  #constructor function
        self.driver = webdriver.Chrome(executable_path="D:\Pandas\chromedriver.exe")  # will initiate driver

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query) #gets the url
        vid = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        vid.click()

#assist = music()
#assist.play('dynamite by bts')