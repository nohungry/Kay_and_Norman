import time

from selenium import webdriver
from bs4 import BeautifulSoup


# 發出網路請求
driver = webdriver.Chrome('/Users/kayzhang/Downloads/python_sql_class/chromedriver')
driver.get('https://www.nike.com/tw/login?continueUrl=https://www.nike.com/tw/member/profile')
time.sleep(3)

# 使用 switch_to.frame 跳出框  PS. 我不確定要沒有框框限制住，但寫了好像也沒有差別.. 所以應該不是這個問題
driver.switch_to.frame("nike-unite-loginForm")

# 試過 find_element_by_id/name/css_selector/xpath 都沒有成功定位到
email = driver.find_element_by_css_selector("#d474faff-8cba-45e0-8928-5eb35ba8d5e2")
email.send_keys('emailAccount')

time.sleep(2)

password = driver.find_element_by_xpath("//*[@id='966a2f30-4015-4b11-8c3a-881a872e7e2a']")
password.send_keys('password')

time.sleep(2)

button = driver.find_elements_by_id('c876cc21-1ad4-4300-8a9d-26d99e20e020')
button.click()


# diver 先行關閉
driver.quit()