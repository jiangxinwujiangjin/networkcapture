
from selenium import webdriver #导入webdriver模块
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#driver = webdriver.Chrome(service=Service(r'D:\chromedriver\chromedriver-win64\chromedriver.exe')) #wbdriver的Chrome类，创建一个webdriver实例对象
driver.get('https://www.google.com')
#选择元素
try:
    element = driver.find_element(By.ID, 'container') #根据ID选择元素
    element.click() #点击
except Exception as e:
    print('find error')
finally:
    print('over')
title = driver.title
print(title)
driver.implicitly_wait(1)