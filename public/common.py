from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\\Tools\\Pycharm\\UI\\driver\\chromedriver.exe")
driver.maximize_window()
driver.get("http:www.baidu.com")