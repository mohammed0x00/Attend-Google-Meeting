import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Retrieve Google credentials from environment variables
email = os.getenv("GOOGLE_EMAIL")
password = os.getenv("GOOGLE_PASSWORD")
meet_url = "https://meet.google.com/your-meet-code"

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def google_login(email, password):
    driver.get("https://accounts.google.com/signin")

    # Enter email
    email_field = driver.find_element(By.ID, "identifierId")
    email_field.send_keys(email)
    email_field.send_keys(Keys.ENTER)
    time.sleep(2)

    # Enter password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)
    time.sleep(5)  # Adjust sleep time as necessary

def join_google_meet(meet_url):
    driver.get(meet_url)
    time.sleep(5)  # Adjust sleep time as necessary

    # Join the meeting (you may need to handle additional buttons depending on the state of your browser/microphone permissions)
    join_button = driver.find_element(By.XPATH, "//span[text()='Join now']")
    join_button.click()

# Log in to Google
google_login(email, password)

# Join Google Meet
join_google_meet(meet_url)

# Keep the browser open for a while
time.sleep(30)

# Close the browser
driver.quit()
