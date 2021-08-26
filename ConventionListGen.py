from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = ".\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://animecons.com/events/schedule.php?year=2021")
