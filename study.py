from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
print("Give the expected time in Minutes:")
try:
    times=int(input())
except ValueError:
    print("Enter Only in Numbers")
    quit()
print("Enter the Subjects you want to study: or type '[regular] for 4-1' or '[previous] for 3-2' or '3-1'")
subjects = [i for i in input().split(" ")]
if subjects[0] =='supply':
    del(subjects)
    subjects=['cao','digital communications','awp']
if subjects[0] =='previous':
    del(subjects)
    subjects=['vlsi','dsp','mwe','mpmc','java']
if subjects[0] =='regular':
    del(subjects)
    subjects=['rs','oc','cn','sdv','dip','aicd']
PATH= "C:\Program Files (x86)\Drivers\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("http://www.google.com")
driver.maximize_window()
page=1
try:
    for subject in subjects:
        if subject == 'cao':
            driver.get("https://www.javatpoint.com/computer-organization-and-architecture-tutorial")
        elif subject == 'java':
            driver.get("https://www.javatpoint.com/exception-handling-in-java")
        elif subject == 'cn':
            driver.get("https://www.javatpoint.com/types-of-computer-network")
        elif subject == 'rs':
            driver.get("https://www.tutorialspoint.com/radar_systems/radar_systems_overview.htm")
        elif subject == 'dip':
            driver.get("https://www.tutorialspoint.com/dip/index.htm")
        elif subject == 'aicd':
            driver.get("https://nptel.ac.in/courses/117/106/117106030/")
        elif subject == 'oc':
            driver.get("https://www.tutorialspoint.com/principles_of_communication/principles_of_optical_fiber_communications.htm")
        elif subject == 'sdv':
            driver.get("https://mrcet.com/downloads/digital_notes/ECE/III%20Year/DIGITAL%20DESIGN%20THROUGH%20VERILOG-18.pdf")
        else:
            search = WebDriverWait(driver,4).until(
                EC.presence_of_element_located((By.NAME,'q'))
            )
            search.send_keys(subject+" tutorialspoint",Keys.RETURN)
            select = driver.find_element_by_class_name("LC20lb.DKV0Md")
            select.click()
        if page < len(subjects):
            driver.execute_script('''window.open("http://google.com","_blank");''')
            driver.switch_to.window(driver.window_handles[page])
            page+=1
        else:
            driver.switch_to.window(driver.window_handles[0])
finally:
    time.sleep(times*60)
    driver.quit()
