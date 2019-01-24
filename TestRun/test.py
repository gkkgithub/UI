# # from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import re,time
# # from PIL import Image,ImageEnhance
# #
# #
# # url = 'https://passport.baidu.com'
# # image_path = 'D:\\Tools\\Pycharm\\UI\\TestData\\image.png'
# # screen =  'D:\\Tools\\Pycharm\\UI\\TestData\\screen.png'
# #
# # Driver = webdriver.Chrome()
# # Driver.maximize_window()
# # wait = WebDriverWait(Driver,5)
# # Driver.get(url)
# # wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="TANGRAM__PSP_3__footerULoginBtn"]'))).click()
# # wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="TANGRAM__PSP_3__submitWrapper"]/a'))).click()
# # # //*[@id="forgotsel"]/div/div[3]/img   //*[@id="forgotsel"]/div/div[3]/img
# # # time.sleep(10)
# # # # code_input = Driver.find_element_by_xpath('//*[@id="account"]')
# # # code_input = Driver.find_element_by_css_selector('#account')
# # # code_input.send_keys('12434')
# # wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submit"]'))).click()
# # print('点击提交')
# #
# # Driver.get_screenshot_as_file(image_path)
# #
# # location = Driver.find_element_by_xpath('//*[@id="forgotsel"]/div/div[3]/img').location
# # size = Driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeImg').size
# # left = location['x']
# # top = location['y']
# # right = location['x'] + size['width']
# # bottom = location['y'] + size['height']
# # # 从文件读取截图，截取验证码位置再次保存
# # img = Image.open(image_path).crop((left, top, right, bottom))
# # img = img.convert('L')  # 转换模式：L | RGB
# # img = ImageEnhance.Contrast(img)  # 增强对比度
# # img = img.enhance(2.0)  # 增加饱和度
# # img.save(screen)
# #
# #
# #
#
#
# import re
# import requests
# # import pytesseract
# from selenium import webdriver
# from PIL import Image, ImageEnhance
#
# username = "xxxxxx"
# password = "xxxxxx"
#
# # chromedriver = 'D:/Python35/selenium/webdriver/chromedriver/chromedriver.exe'
# loginurl = 'https://passport.baidu.com/v2/?login'
#
# # 截图或验证码图片保存地址
# screenImg = "D:\\Tools\\Pycharm\\UI\\TestData\\screen.png"
# screenImg1 = "D:\\Tools\\Pycharm\\UI\\TestData\\screen1.png"
# # 打开浏览器
# Driver = webdriver.Chrome()
# Driver.maximize_window()
#
# Driver.get(loginurl)
# Driver.implicitly_wait(1)
#
# # cookie= Driver.get_cookies()
# assert "登录百度帐号" in Driver.title
# wait = WebDriverWait(Driver,5)
# wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="TANGRAM__PSP_3__footerULoginBtn"]'))).click()
# # 数据账号&密码(此处不提交)
# time.sleep(5)
# for num in range(10):
#     a = Driver.find_element_by_id("TANGRAM__PSP_3__userName")
#     a.clear()
#     a.send_keys(username)
#     b =  Driver.find_element_by_id("TANGRAM__PSP_3__password")
#     b.clear()
#     b.send_keys(password)
#
#     # 用于测试，此处可提前提交，让登录出错，页面出现验证码
#     Driver.find_element_by_id("TANGRAM__PSP_3__submit").click()
#     time.sleep(3)
#
# # 获取验证码URL地址
# imgsrc = Driver.find_element_by_id("TANGRAM__PSP_3__verifyCodeImg").get_attribute('src')
# print(imgsrc)
#
# # 如果匹配验证码路径成功（说明有提示输入验证码），则需读取验证码！
# if re.match(r'https://passport.baidu.com/cgi-bin/genimage.*', imgsrc):
#     # 浏览器页面截屏
#
#     Driver.get_screenshot_as_file(screenImg)
#     # 定位验证码位置及大小
#     location = Driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeImg').location
#     size = Driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeImg').size
#
#     left = location['x']
#     top = location['y']
#     right = location['x'] + size['width']
#     bottom = location['y'] + size['height']
#     print(location,left,top,right,bottom,size)
#     # 从文件读取截图，截取验证码位置再次保存
#     img = Image.open(screenImg).crop((left, top, right, bottom))
#     img = img.convert('L')  # 转换模式：L | RGB
#     img = ImageEnhance.Contrast(img)  # 增强对比度
#     img = img.enhance(2.0)  # 增加饱和度
#     img.save(screenImg1)
#     # 再次读取识别验证码
#     img = Image.open(screenImg)
#
#

import requests


url = 'http://47.100.11.197:7004/api/loan/dataflow/rong360/order/basic/push'

re = requests.post(url=url)
print(re.status_code)
