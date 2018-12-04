from selenium import webdriver
from time import sleep




driver = webdriver.Chrome(executable_path="D:\\Tools\\Pycharm\\UI\\driver\\chromedriver.exe")
driver.maximize_window()
driver.get("http:www.baidu.com")
sleep(5)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("测试教程网")
sleep(1)
driver.find_element_by_xpath('//*[@id="su"]').click()
print("输入测试教程网，点击搜索按钮")
assert "测试教程网_百度搜索" == driver.title
assert "[优惠活动]" in driver.page_source
