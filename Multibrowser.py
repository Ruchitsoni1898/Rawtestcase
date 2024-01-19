from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Note the capital 'K'
from selenium.webdriver.chrome.options import Options
chrome_driver_path = "D:\\chromedriver-win64\\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument(f"executable_path={chrome_driver_path}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()