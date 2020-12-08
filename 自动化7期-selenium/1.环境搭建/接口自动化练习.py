#---------------
#姓名：孟繁荣
#电话：13049337834
#---------------
# import requests
# test_url = "http://www.baidu.com"
# response = requests.get(test_url)
# print(response.status_code)
# print(response.headers)
# print(response.text)
# 1）加密算法
# import hashlib
# import random
# oldpass = 123456
# salt = random.randrange(0,10)
# print(salt)
# h1=hashlib.sha224(b'oldpass+salt')
# print(oldpass+salt)
# newpass=h1.hexdigest()
# print(newpass)
# print(oldpass)
# 2）UI自动化练习
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_xpath("//input[@id='kw']").send_keys("UI")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='su']").click()
time.sleep(3)
driver.close()
