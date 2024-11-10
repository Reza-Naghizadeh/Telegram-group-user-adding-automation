import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re


# Different time management
def one_to_five_sec():
        t = random.randint(1, 5)
        time.sleep(t)


def ten_to_twenty_sec():
        t = random.randint(10, 20)


def one_min():
        time.sleep(60)


def ten_min():
        time.sleep(10 * 60)


def one_hour():
        time.sleep(60 * 60)


def two_hour():
        time.sleep(2 * (60 * 60))


def phone_number_checker(phone_number):
        pattern = re.compile(r'^9\d{9}$')

        if not pattern.match(str(phone_number)):
                return False
        else:
                initial = '+98'
                pn = initial + str(phone_number)

                return pn


def page_loader(driver, page):
        try:
                driver.get(page)
        except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == '__main__':

        # ############################### READ THE PHONE NUMBERS ###############################
        df = pd.read_excel('/Users/reza/Programming/thesis_codes/Telegram_add/numbers.xlsx', header=None,names=['name', 'phone'])
        # ############################### READ THE PHONE NUMBERS ###############################

        # ############################### LOG IN ###############################
        # Set the path to your webdriver (e.g., chromedriver)
        webdriver_path = '/Users/reza/Programming/extra_files/geckodriver'

        chrome_options = Options()

        # Set the path to chromedriver using the add_argument method
        chrome_options.add_argument(f'--executable_path={webdriver_path}')

        website = 'https://web.telegram.org/'

        drivers = {}
        num_drivers = 2
        for i in range(1, num_drivers + 1):
                driver_name = f'driver{i}'
                drivers[driver_name] = webdriver.Chrome(options=chrome_options)
                drivers[driver_name].get(website)
                time.sleep(20)

        # ############################### LOG IN ###############################

        # ############################### MAIN PART ###############################
        wait_time = 120
        counter = 0
        driver_num = 1
        for i in range(df.shape[0]):
                print(i)
                driver_name = f'driver{driver_num}'
                if counter % 2 == 0 and counter != 0:
                        print('Counter reset')
                        # two_hour()
                        one_min()
                        counter = 0
                        drivers[driver_name].minimize_window()
                        if driver_num < num_drivers:
                                driver_num += 1
                        else:
                                driver_num = 1

                name = df.iloc[i, 0]
                phone_number = df.iloc[i, 1]
                phone_number = phone_number_checker(phone_number)

                if not phone_number:
                        continue
                else:

                        driver_name = f'driver{driver_num}'
                        drivers[driver_name].refresh()
                        time.sleep(20)

                        # ############################### ADDING CONTACT ###############################
                        try:
                                # Click on ADD USER
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//button[@title='Create New Contact']//i[@class='icon icon-add-user-filled']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()
                        except Exception as e:
                                # Click on HAMBURGER
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//button[@title='Open menu']//div[@class='ripple-container']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()

                                # Click on CONTACTS
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//div[normalize-space()='Contacts']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()

                                # Click on ADD USER
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//button[@title='Create New Contact']//i[@class='icon icon-add-user-filled']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()

                        # ############################### ADDING CONTACT ###############################
                        one_to_five_sec()
                        try:
                                # Fill the phone number
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//input[@aria-label='Phone Number']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.send_keys(phone_number)

                                one_to_five_sec()

                                # Fill the name
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//input[@aria-label='First name (required)']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.send_keys(name)

                                one_to_five_sec()

                                # Click on Done
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//button[normalize-space()='Done']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()
                                try:
                                        # Check the notification for non-registered users
                                        wait = WebDriverWait(drivers[driver_name], wait_time)
                                        element_css_selector = "//div[@class='Notification opacity-transition fast open shown']//div[@class='content']"
                                        element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))

                                        one_to_five_sec()

                                        # Click on Cancel
                                        wait = WebDriverWait(drivers[driver_name], wait_time)
                                        element_css_selector = "//button[normalize-space()='Cancel']"
                                        element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                        element.click()

                                        continue

                                except Exception as e:
                                        pass

                        except Exception as e:
                                pass

                        one_to_five_sec()

                        counter += 1

                        # ############################### PAGE HANDLING ###############################
                        page_loader(drivers[driver_name], 'https://t.me/germililar2')
                        # Click on open web app
                        wait = WebDriverWait(drivers[driver_name], wait_time)
                        element_css_selector = "//span[@class='tgme_action_button_label']"
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                        element.click()
                        # ############################### PAGE HANDLING ###############################

                        # ############################### ADDING USER TO THE GROUP ###############################
                        try:
                                # Click on the name of group
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//div[@class='ChatInfo']//div[@class='title ysHMmXALnn0fgFRc7Bn7']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()

                                time.sleep(2)

                                # Click on Adding user to group
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//i[@class='icon icon-add-user-filled']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()

                                time.sleep(2)

                                # Fill the search box
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//input[@id='new-members-picker-search']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.send_keys(name)

                                one_to_five_sec()

                                # Click on user's name
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//div[@role='button']//div[@class='ripple-container']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()

                                time.sleep(2)

                                # Click on final add button
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//i[@class='icon icon-arrow-right']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()

                                try:
                                        # Click on privacy OK
                                        wait = WebDriverWait(drivers[driver_name], wait_time)
                                        element_css_selector = "div[id='portals'] button:nth-child(1)"
                                        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_css_selector)))
                                        page_loader(drivers[driver_name], website)

                                except Exception as e:
                                        pass

                        except Exception as e:
                                # Click on Adding user to group
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//i[@class='icon icon-add-user-filled']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()

                                # Fill the search box
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//input[@id='new-members-picker-search']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.send_keys(name)

                                one_to_five_sec()

                                # Click on user's name
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//div[@role='button']//div[@class='ripple-container']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()

                                time.sleep(2)

                                # Click on final add button
                                wait = WebDriverWait(drivers[driver_name], wait_time)
                                element_css_selector = "//i[@class='icon icon-arrow-right']"
                                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_css_selector)))
                                element.click()

                                try:
                                        # Click on privacy OK
                                        wait = WebDriverWait(drivers[driver_name], wait_time)
                                        element_css_selector = "div[id='portals'] button:nth-child(1)"
                                        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_css_selector)))
                                        page_loader(drivers[driver_name], website)

                                except Exception as e:
                                        pass

                        # ############################### ADDING USER TO THE GROUP ###############################

                # ############################### MAIN PART ###############################
