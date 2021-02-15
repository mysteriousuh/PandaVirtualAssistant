from selenium import webdriver

class infow(): #class knowm as info
    def __init__(self):  #constructor function
        self.driver = webdriver.Chrome(executable_path="D:\Pandas\chromedriver.exe")  # will initiate driver

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/") #gets the url
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/button/i')
        enter.click()




