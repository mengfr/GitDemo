#---------------
#姓名：孟繁荣
#电话：13049337834
#---------------
#第一道题目请一直向下看：
#id元素定位
# from selenium import webdriver
# import time
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com/")
#id元素定位
# time.sleep(2)#等待两秒
# drive.find_element_by_id("kw").send_keys("selenium")#根据ID元素定位在输入框输入selenium
# time.sleep(2)#等待两秒
# drive.find_element_by_id("kw").click()#输入后点击百度
# time.sleep(2)#等待两秒
# drive.close()#关闭所有页面

# #name元素定位
# driver.find_element_by_name("wd").send_keys("selenium")
# time.sleep(3)
# driver.find_element_by_name("wd").click()
# time.sleep(3)
# driver.close()

#class元素定位
# driver.find_element_by_class_name("s_ipt").send_keys("selenium")
# driver.find_element_by_class_name("s_ipt").click()
# time.sleep(3)
# driver.close()

#xpath元素定位
#1、绝对路径定位元素
# driver.find_element_by_xpath(r"html/body/div/div/div/div/div/form/span/input[@id='kw']").send_keys("selenium")
# #2、相对路径定位元素
# driver.find_element_by_xpath("//input[@id='kw']").click()
# time.sleep(3)
# driver.close()

#css 元素定位
#方法1
#1、css，id名称定位
# driver.find_element_by_css_selector("input#kw").send_keys("selenium")
# #2.相对路径定位元素
# driver.find_element_by_css_selector("input[value='百度一下']").click()
# time.sleep(3)
# driver.close()
#方法2 css-class名称元素定位法
driver.find_element_by_css_selector("input.s_ipt").send_keys("selenium")
#2.相对路径定位元素
driver.find_element_by_css_selector("input[value='百度一下']").click()
time.sleep(3)
driver.close()