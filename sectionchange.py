from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException
import ctypes  # An included library with Python install.   
import sys
####################################
#Using your python console, install the required package with following command:
#pip install selenium
####################################
course_indice = '2' #Your course indice, namely the order of your course among the bulletpoints. Use 1 for the first and 2 for the second.
#Having x courses, one can select between 1-x as their indice value, which represents the location of their course indice on register.metu.edu.tr
desired_section = '2' #Insert your desired section here
username = 'username' #Your username in the format 'eXXXXXX'
password = 'password' #Your password
course_category = 'NONTECHNICAL ELECTIVE' #Choose between the Course Category section. Following are valid: 'MUST', 'RESTRICTED ELECTIVE', 'FREE ELECTIVE', 'TECHNICAL ELECTIVE', 'NONTECHNICAL ELECTIVE', 'NOT INCLUDED'.
driver = webdriver.Chrome('C:/Users/ardaa/OneDrive/Masaüstü/chromedriver') #Locate your chromedriver. You can find the source at https://chromedriver.chromium.org/
#Any misspell among tese strings might end up in an error.
####################################

actual_indice = str((int(course_indice)+1))
driver.get("https://register.metu.edu.tr")
time.sleep(1)
def login(Username,Password):
    driver.get("https://register.metu.edu.tr")
    time.sleep(1)
    usernameBox = driver.find_element_by_xpath('//*[@id="textUserCode"]')
    passwordBox = driver.find_element_by_xpath('//*[@id="textPassword"]')
    usernameBox.send_keys(Username)
    passwordBox.send_keys(Password)
    driver.find_element_by_xpath('//*[@id="single_content"]/form/div/div/input[3]').click()
    spam()

def spam():
    try:
        while driver.find_element_by_xpath('//*[@id="single_content"]/form/table[3]/tbody/tr[1]/td/table/tbody/tr['+actual_indice+']/td[5]').get_attribute('textContent') != desired_section:
            driver.find_element_by_xpath('//*[@id="single_content"]/form/table[3]/tbody/tr[1]/td/table/tbody/tr['+actual_indice+']/td[1]/input').click()
            time.sleep(1)
            if driver.find_element_by_xpath('//*[@id="textChangeCourseSection"]').get_attribute('value') != desired_section:
                driver.find_element_by_xpath('//*[@id="textChangeCourseSection"]').send_keys(desired_section)
            time.sleep(1)
            Select(driver.find_element_by_xpath('//*[@id="selectChangeCourseCategory"]')).select_by_visible_text(course_category)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="single_content"]/form/div[2]/div/center/fieldset/div/table/tbody/tr[2]/td[2]/input').click()
        else:
            
             ctypes.windll.user32.MessageBoxW(0, "Sectionı aldın hokam tarayıcıyı kapatabilirsin", "HUHA", 1)
             sys.exit()
        
    except NoSuchElementException:
        login(username,password)

login(username,password)


        