from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random


service = Service('C:/Users/rotem/Desktop/bots/unfollow-auto/chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service=service)

driver.get('https://www.instagram.com/accounts/login/')
sleep(random.randint(3, 6)) 

# creds
USERNAME = driver.find_element(By.NAME, "username")
PASSWORD = driver.find_element(By.NAME, "password")
USERNAME.send_keys("username")  # YOUR USERNAME
PASSWORD.send_keys("pwd")  # YOUR PASSWORD
driver.find_element(By.XPATH, "//button[@type='submit']").click()
sleep(random.randint(5, 10))  

# handle potential popups 
try:
    save_info_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
    )
    save_info_button.click()
    sleep(2)
    print("Save Info popup handled.")
except Exception:
    print("No Save Info popup.")

try:
    notifications_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
    )
    notifications_button.click()
    sleep(2)
    print("Notifications popup handled.")
except Exception:
    print("No Notifications popup.")

# reading the users list
with open('unfollow_list.txt', 'r') as file:
    unfollow_users = file.readlines()


unfollow_users = [user.strip() for user in unfollow_users]


for user in unfollow_users:
    print(f"Processing {user}...")

    # opening the current user's ig
    driver.get(f"https://www.instagram.com/{user}/")
    sleep(random.randint(10, 20))  

    # debugging
    print("Checking if 'Following' button is present...")

    try:
        following_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_acan') and .//div[contains(text(), 'Following')]]"))
        )
        print("Following button is clickable.")
        following_button.click()
        sleep(random.randint(2, 5))  

        # unfollowing
        unfollow_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Unfollow']"))
        )
        print("Unfollow button found.")
        unfollow_button.click()
        sleep(random.randint(3, 6))  

        print(f"Successfully unfollowed {user}!")
    except Exception as e:
        print(f"Error unfollowing {user}: {e}")

driver.quit()
