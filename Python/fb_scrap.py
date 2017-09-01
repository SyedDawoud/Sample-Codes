from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class FacebookScraper:

    def __init__(self):
        self.scrapDataDict={}
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")
       

        
    # Closing the driver after completing the task
    def close_driver(self):
        self.driver.quit()

    # Get any specific data from dictionary based on the key
    def get_specific_dict_data(self,key):
        try:
            return self.scrapDataDict[key]
        except Exception as e:
            print (e)
            return "Entry Not Found"

        
    # Get the Whole Dictionary
    def getscrapDataDict(self):
        return self.scrapDataDict

    # Set the Number of Likes after loading fb page, inside the data Dictionary
    def storeNumberofLikes(self):
        try:
            self.scrapDataDict["likes"]=self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div").get_attribute("innerHTML")      
        except Exception as e:
            print(e)
            self.scrapDataDict["likes"]="N/A"

    # Set the Number of following, inside data dictionary

    def storeNumberofFollowing(self):
        try:
            self.scrapDataDict["following"]=self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div").get_attribute("innerHTML")
        except Exception as e:
            print(e)
            self.scrapDataDict["following"]="N/A"

    
    
    # Set The Number of Visits

    def storeNumberofVisits(self):
        try:
            self.scrapDataDict["visits"]=self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/div[4]/div/div[2]/div").get_attribute("innerHTML")
        except Exception as e:
            print(e)
            self.scrapDataDict["visits"]="N/A"

    def storeRating(self):
        try:
            self.scrapDataDict["rating"]=self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/span").get_attribute("innerHTML")
        except Exception as e:
            print(e)
            self.scrapDataDict["rating"]="N/A"

    def storeReview(self):
        try:
            self.scrapDataDict["review"]=self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/span").get_attribute("innerHTML")
        except Exception as e:
            print(e)
            self.scrapDataDict["review"]="N/A"
    

    # html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/span

    # html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/span
        
    # Scrap information from facebook of a particular brand
    def searchBrand(self,brand_name):
        # Submit the search query on google
        element = self.driver.find_element_by_name("q")
        element.send_keys(brand_name+" "+"facebook")
        element.submit()
        # Wait for the page to load
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "resultStats")))
        # Get the top most result and click it
        fb_result=self.driver.find_element_by_xpath("(//h3[@class='r']/a)[1]").click()
        # Get the new url
        time.sleep(5)
        new_url=(self.driver.current_url)
        # Some Special FB Fields
        isPresent1=len(self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div").get_attribute("innerHTML"))!=0
        isPresent2=len(self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div").get_attribute("innerHTML"))!=0
        print (new_url)
        if "facebook" not in new_url or not isPresent1 or not isPresent2:
            print("Not Facebook Page")
        else:
            print("facebook url for Page is:" + new_url)
            # Calling the Data Scraping Functions after getting the url
            self.storeNumberofLikes()
            self.storeNumberofFollowing()
            self.storeNumberofVisits()
            self.storeRating()
            self.storeReview()
            



fbscrap=FacebookScraper()
fbscrap.searchBrand("Engineer's Kitchen")
data_dict=fbscrap.getscrapDataDict()

for k,v in data_dict.iteritems():
    print(k +" : " + v)

