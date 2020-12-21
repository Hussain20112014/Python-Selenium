from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
print(driver.title)

driver.get("https://www.marefa.org/%D9%85%D8%AD%D9%85%D8%AF_%D9%85%D9%87%D8%AF%D9%8A_%D8%A7%D9%84%D8%AC%D9%88%D8%A7%D9%87%D8%B1%D9%8A")





li = driver.find_element_by_id("ca-talk")
li.click()

driver.get("https://PinkVillainousVoxel.hussain2011.repl.co")

li2 = driver.find_element_by_id("ca-viewsource")
li2.click()

