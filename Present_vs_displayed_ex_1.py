from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "C:///Users/49157/PycharmProjects/SeleniumProject/present_vs_displayed.html"

driver.get(url)

my_btn1 = driver.find_element("id","btn1")
my_btn_txt = my_btn1.text
print("first button text:{}".format(my_btn_txt))

my_btn2 = driver.find_element("id","btn2")
my_btn2_txt = my_btn2.text
print("second button text:{}".format(my_btn2_txt))

my_btn3 = driver.find_element("id","btn3")
my_btn3_txt = my_btn3.text
print("Third button text:{}".format(my_btn3_txt))

my_btn4 = driver.find_element("id","btn4")
my_btn4_txt = my_btn4.text
print("Fourth button text:{}".format(my_btn4_txt))

if my_btn4.is_displayed():
    my_btn4.click()
raise Exception("Button 4 is not displyed")


import pdb
pdb.set_trace()