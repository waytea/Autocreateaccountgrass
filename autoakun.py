import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def clickleave(driver):
    try:
        leave_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "chakra-button") and contains(@class, "css-xxce40")]'))
        )
        leave_button.click()
    except Exception as e:
        print(f"Click leave failed: {e}")

def profile(driver):
    driver.get("https://app.getgrass.io/dashboard/profile")

def logout(driver):
    try:
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "chakra-button") and contains(@class, "css-1h1k2zj")]'))
        )
        logout_button.click()
        print("Successfully logged out.")
    except Exception as e:
        print(f"Logout failed: {e}")

def human_delay(min_seconds=1, max_seconds=3):
    time.sleep(random.uniform(min_seconds, max_seconds))

# Baca email dan username dari file
with open('email.txt', 'r') as email_file:
    emails = email_file.readlines()
with open('username.txt', 'r') as username_file:
    usernames = username_file.readlines()

password = "Rionaldi18*"

# Konfigurasi WebDriver dengan uc
options = uc.ChromeOptions()
options.add_argument('--start-maximized')

driver = uc.Chrome(options=options)

try:
    for email, username in zip(emails, usernames):
        email = email.strip()
        username = username.strip()

        driver.get("https://app.getgrass.io/register?referralCode=rg-b-f6CN6nuLfP")

        # Tunggu hingga elemen input email tersedia
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.clear()
        email_input.send_keys(email)
        human_delay()

        # Tunggu hingga elemen input username tersedia
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_input.clear()
        username_input.send_keys(username)
        human_delay()

        # Tunggu hingga elemen input password tersedia
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.clear()
        password_input.send_keys(password)
        human_delay()

        # Tunggu hingga elemen input konfirmasi password tersedia
        confirm_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "confirmPassword"))
        )
        confirm_password_input.clear()
        confirm_password_input.send_keys(password)
        human_delay()

        # Tunggu selama 45 detik
        time.sleep(45)

        # Coba ambil user_id dari localStorage dan tangani kemungkinan masalah
        try:
            user_id = driver.execute_script("return localStorage.getItem('userId');")
            if user_id:
                print("User ID:", user_id)
                # Tulis User ID ke file teks
                with open("user_id.txt", "a") as file:
                    file.write(user_id + "\n")
            else:
                print("User ID tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat mengambil User ID: {e}")

        profile(driver)
        clickleave(driver)
        logout(driver)
        
        time.sleep(5)

finally:
    driver.quit()
