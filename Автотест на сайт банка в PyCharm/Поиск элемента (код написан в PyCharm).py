from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/")
driver.set_window_size(1366, 768)
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "login-otp-button").click()

messagebutton = driver.find_element(By.ID, "messages-button")
if messagebutton is None:
    print("Элемент Письма не имеется")
else:
    print("Элемент Письма имеется")

time.sleep(5)