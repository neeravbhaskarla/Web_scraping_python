


# This is for only ECE subjects from 3-1




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
print("Enter the Subjects you want to study: or type '[regular] for 3-2' and '[supply] for 3-1' ")
subjects = [i for i in input().split(" ")]
if subjects[0] =='supply':
    del(subjects)
    subjects=['cao','digital communications','awp']
if subjects[0] =='regular':
    del(subjects)
    subjects=['vlsi','dsp','mwe','mpmc','java']
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