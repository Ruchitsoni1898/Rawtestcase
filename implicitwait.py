from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\chromedriver-win64\\chromedriver.exe")

driver.get("https://demo.guru99.com/test/newtours/")
assert "Welcome: Mercury Tours" in driver.title
driver.implicitly_wait(10)
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("submit").click()
