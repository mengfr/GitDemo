#---------------
#姓名：孟繁荣
#电话：13049337834
#---------------
#conding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()#驱动火狐浏览器
driver.get("http://www.sogou.com")#使用浏览器搜索网址
time.sleep(3)#等待三秒
driver.find_element_by_id("query").send_keys("selenium")#元素定位，在搜索框输入selenium
driver.find_element_by_id("stb").click()#点击搜索
time.sleep(3)#等待三秒
driver.find_element_by_id("top_qreset").click()#点击清除按钮
time.sleep(3)#等待三秒
driver.find_element_by_id("upquery").send_keys("python")#清除后在搜索框输入Python
time.sleep(3)#等待三秒
driver.find_element_by_id("searchBtn").click()#点击搜索
time.sleep(3)#等待三秒
driver.close()#关闭所有打开浏览页面



