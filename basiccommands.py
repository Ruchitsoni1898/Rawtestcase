from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "D:\\chromedriver-win64\\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument(f"executable_path={chrome_driver_path}")

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.msn.com/de-de")
    driver.find_element_by_name("q").send_keys("selenium")
    driver.find_element_by_name("btnK").submit()  # Make sure this is the correct name
    driver.close()

except Exception as e:
    print(f"An error occurred: {e}")
