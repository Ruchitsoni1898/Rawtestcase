from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
time.sleep(2)
url ='http://demostore.supersqa.com/my-account/'

email_field = "reg_email"
pass_field = "reg_password"
logout_btn = "li.woocomerce-Myaccount-navigation-link--customer-logout-a"
driver.get(url)
email_field = driver.find_element(By.ID,email_field)


# generate random email
letters = string.ascii_lowercase
rand_string = "".join(random.choice(letters)for i in range(15))
random_email = rand_string + "@supersqa.com"

#type in the email field
email_field.send_keys(random_email)

# find password field and enter password
pass_field = driver.find_element(By.ID,pass_field)
pass_field.send_keys("mynewpassword!1")

time.sleep(2)
register_btn = driver.find_element(By.CSS_SELECTOR,'button[value="Register"]')
register_btn.click()

logout_btn = driver.find_element(By.CSS_SELECTOR,logout_btn_css)
if logout_btn.is_displayed():
    print("pass")
else:
    raise Exception("User not logged in after registration")
