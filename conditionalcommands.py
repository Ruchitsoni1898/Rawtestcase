from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/")
usr_ele = driver.find_element_by_name("userName")
print(usr_ele.is_displayed())
print(usr_ele.is_enabled())

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

usr_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

# Now, find and click the submit button
driver.find_element_by_name("submit").click()

# Rest of your code...
roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of round trip radio button", roundtrip_radio.is_selected())
one_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("status of one way radio button", one_radio.is_selected())
