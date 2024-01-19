from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InvalidLoginError:
    url ="http://demostore.supersqa.com/my-account/"
    invalid_email = "abc@supersqa.com"
    expected_msg = "Error: The password you entered for the email address abc@supersqa.com is incorrect. Lost your password?"
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    def go_to_my_account(self):
        self.driver.get(self.url)

    def input_email(self):
        field = self.driver.find_element(By.ID,'username')
        field.send_keys(self.invalid_email)
        pass
    def input_pass(self):
        field = self.driver.find_element(By.ID,'password')
        field.send_keys("abcdefg")
        pass

    def click_login(self):
        self.driver.find_element(By.NAME,"login").click()
        pass

    def verify_user_message(self):
        err_elm = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
        displayed_msg = err_elm.text
        assert displayed_msg == self.expected_msg,"the displayed error is not expected"
        print("Pass")
        pass

    def main(self):
       self.go_to_my_account()
       self.input_email()
       self.input_pass()
       self.click_login()
       self.verify_user_message()
       self.driver.quit()

if __name__ == '__main__':
       obj = InvalidLoginError()
       obj.main()
