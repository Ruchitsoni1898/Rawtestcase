import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
driver.get("https://www.msn.com/de-de")
time.sleep(5)
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)