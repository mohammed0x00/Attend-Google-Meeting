import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Retrieve Google credentials from environment variables
email = os.getenv("GOOGLE_EMAIL")
password = os.getenv("GOOGLE_PASSWORD")
meet_url = "https://meet.google.com/vrt-aquf-pho"

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

def google_login(email, password):
    driver.get("https://accounts.google.com/signin")

    # Enter email
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_field.send_keys(email)
    email_field.send_keys(Keys.ENTER)

    # Wait for the transition to the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)

def join_google_meet(meet_url):
    driver.get(meet_url)
    
    # Wait for the "Join now" button to become clickable
    join_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Join now']"))
    )
    join_button.click()

# Log in to Google
google_login(email, password)

# Join Google Meet
join_google_meet(meet_url)

# Keep the browser open for a while
time.sleep(30)

# Close the browser
driver.quit()
