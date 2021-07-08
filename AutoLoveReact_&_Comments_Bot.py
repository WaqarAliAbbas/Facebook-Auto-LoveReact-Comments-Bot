# Author : Waqar Ali Abbas
# Python Automation Tool
# Facebook Auto Love React And Comments Bot 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key,Controller
import time
print("Note: Please don't perform any action during executing this program...")
print("Tool Developer Waqar Ali Abbas...")
fb_email=input("Email Address:  ")
fb_password=input("Password:  ")
option=Options()
option.add_argument("disable-notifications")
driver=webdriver.Chrome(options=option)
driver.get("https://en-gb.facebook.com/")
email=(By.NAME,"email")
password=(By.NAME,"pass")
login=(By.NAME,"login")
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((email))).send_keys(fb_email)
wait.until(EC.presence_of_element_located((password))).send_keys(fb_password)
wait.until(EC.element_to_be_clickable((login))).click()
time.sleep(5)
keyboard=Controller()
time.sleep(5)
x=0
while True:
    keyboard.press("j")
    keyboard.release("j")
    time.sleep(3)
    keyboard.press("l")
    keyboard.release("l")
    time.sleep(1)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    keyboard.press("c")
    keyboard.release("c")
    time.sleep(3)
    keyboard.type("<3")
    time.sleep(3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(3)
    x+=1
    if x==25:
        keyboard.press(Key.f5)
        keyboard.press(Key.f5)
        time.sleep(3)
        x=0
# -- Developer Waqar Ali Abbas --
