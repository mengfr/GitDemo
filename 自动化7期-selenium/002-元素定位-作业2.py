#---------------
#姓名：孟繁荣
#电话：13049337834
#---------------
#---------------
#姓名：孟繁荣
#电话：13049337834
#---------------
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com/")
#进入百度搜索网址，点击百度新闻
driver.find_element_by_link_text("新闻").click()
time.sleep(2)
#打开第一条新闻
driver.find_element_by_partial_link_text("@全体党员").click()
time.sleep(2)
#获取所有窗口信息
windows = driver.window_handles
#打开新闻浏览页窗口
driver.switch_to.window(windows[-2])
time.sleep(3)
#打开另一条新闻
driver.find_element_by_partial_link_text("中国坚持平等").click()
time.sleep(2)
#等待后，关闭所有
time.sleep(3)
driver.quit()




