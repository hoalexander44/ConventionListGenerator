from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = ".\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://animecons.com/events/schedule.php?loc=us&year=2021")
con_list_table_element = driver.find_element_by_id("ConListTable")

# odd and even doesn't matter its just how the website organized it
conventions = con_list_table_element.find_elements_by_class_name("even")
oddConventions = con_list_table_element.find_elements_by_class_name("odd")

conventions.extend(oddConventions)

for convention in conventions:
	print(convention.text)

driver.quit()

