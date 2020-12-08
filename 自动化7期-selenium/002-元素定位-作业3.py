#---------------
#姓名：孟繁荣
#电话：13049337834
#---------------
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
#进入百度页面点击设置
driver.find_element_by_link_text("设置").click()
time.sleep(2)
#选择搜索设置
driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)
driver.find_element_by_id("nr").click()
time.sleep(2)
#选择每页显示条数为50条
link1 = Select(driver.find_element_by_id("nr"))
link1.select_by_visible_text("每页显示50条")
time.sleep(3)
#保存设置并退出
driver.find_element_by_link_text("保存设置")
time.sleep(3)
driver.quit()
