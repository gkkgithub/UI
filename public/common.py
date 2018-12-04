from selenium import webdriver




driver = webdriver.Chrome(executable_path="D:\\Tools\\Pycharm\\UI\\driver\\chromedriver.exe")
driver.maximize_window()
driver.get("http:www.baidu.com")