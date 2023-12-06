from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Note the capital 'K'

driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()