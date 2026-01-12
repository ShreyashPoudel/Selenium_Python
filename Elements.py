from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get('https://www.google.com')
# googleSearchBox = driver.find_element(By.ID, 'APjFqb')
# googleSearchBox.send_keys('Automation')
# # driver.find_element(By.NAME,'btnK').click()
# googleSearchBox.send_keys(Keys.RETURN)

driver.get('http://trytestingthis.netlify.app/')
# fill firstname and lastname
driver.find_element(By.ID, 'fname').send_keys("Shreyash")
driver.find_element(By.ID, 'lname').send_keys("Poudel")

# select gender
driver.find_element(By.ID, 'male').click()

# select option
select_element = driver.find_element(By.NAME, 'Optionwithcheck[]')
select = Select(select_element)
select.select_by_visible_text('Option 2')


time.sleep(2)