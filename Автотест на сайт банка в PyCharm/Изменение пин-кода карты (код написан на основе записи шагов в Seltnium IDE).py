from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get ("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
driver.set_window_size(1816, 1400)
driver.find_element(By.ID, "login-button").click()
time.sleep(1)
driver.find_element(By.ID, "login-otp-button").click()
time.sleep(1)
driver.execute_script("window.scrollTo(0,17)")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".calendar-event:nth-child(4) .month").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#card-details-ownbank-10072 .card-set-pin > .link-title").click()
time.sleep(1)
driver.find_element(By.ID, "calculator-button-1").click()
time.sleep(1)
driver.find_element(By.ID, "calculator-button-2").click()
time.sleep(1)
driver.find_element(By.ID, "calculator-button-3").click()
time.sleep(1)
driver.find_element(By.ID, "calculator-button-6").click()
time.sleep(1)
driver.find_element(By.ID, "set-pin").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".icon-close").click()
time.sleep(5)