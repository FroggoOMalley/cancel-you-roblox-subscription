from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


driver.get("https://www.roblox.com/login")

try:
    
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    
    username.send_keys("BrightESESE")  
    password.send_keys("Sasis22363")  
    password.send_keys(Keys.RETURN)

    
    time.sleep(2)  
    driver.get("https://www.roblox.com/my/account#!/subscriptions")
    time.sleep(2)
    driver.switch_to.frame(0)
    try:
    
        cancel_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="subscription-management-container"]/div/div[1]/button/span'))
        )
        cancel_button.click()
        print("Clicked cancel subscription button.")

       
        confirm_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Confirm')]"))
        )
        confirm_button.click()
        print("Subscription cancellation confirmed.")

    except (NoSuchElementException, TimeoutException):
        print("cant find that element :3 .")

except (NoSuchElementException, TimeoutException):
    print("time out ")


time.sleep(5)
driver.quit()