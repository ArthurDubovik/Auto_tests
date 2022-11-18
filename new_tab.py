from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)
button1 = browser.find_element(By.TAG_NAME, "button")
button1.click()
print(browser.window_handles)
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = browser.find_element(By.ID, "input_value").text
answer = browser.find_element(By.ID, "answer")
answer.send_keys(calc(x))
button2 = browser.find_element(By.TAG_NAME, "button")
button2.click()
