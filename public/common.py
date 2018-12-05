from selenium import webdriver
from time import sleep




driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http:www.baidu.com")
sleep(5)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("测试教程网")
sleep(1)
driver.find_element_by_xpath('//*[@id="su"]').click()
print("输入测试教程网，点击搜索按钮,等待5秒")
sleep(5)
print(driver.title)
assert "测试教程网_百度搜索" == driver.title
print('判断页面title是否正确')
driver.quit()
print('hello world')
print('回滚到指定版本')
print('回滚到指定版本一')

