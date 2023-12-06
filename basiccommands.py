import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(4)
print(driver.title)
print(driver.current_url)
#driver.close()
driver.quit()
