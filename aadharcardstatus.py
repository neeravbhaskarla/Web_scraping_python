from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\Drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://resident.uidai.gov.in/check-aadhaar")
driver.maximize_window()
id = driver.find_element_by_id("enrolmentid")
id.send_keys("") # Enter your aadhar card number here
id.send_keys(Keys.ENTER)
time.sleep(30)
driver.quit()
