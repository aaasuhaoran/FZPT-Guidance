import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 判断当前是否联网
try:
    response = requests.get("https://www.baidu.com")
    print("当前设备已联网")
except:
    driver = webdriver.Firefox()
    driver.get("http://202.106.0.20:90")
    
    # 输入用户名
    email_element = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.ID, "username")))
    email_element.clear()
    email_element.send_keys("wangyuntao@spacechina.com")
    driver.implicitly_wait(1)

    # 输入密码
    email_element = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.ID, "password1")))
    email_element.clear()
    email_element.send_keys("请输出你的密码")
    driver.implicitly_wait(1)

    # 左键登录
    login_element = WebDriverWait(driver, timeout=10).until(
                    EC.presence_of_element_located((By.ID, "submit_button_1")))
    login_element.click()

    driver.close()
    
