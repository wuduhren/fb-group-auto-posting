# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



def main():
    account = "YOUR_FACEBOOK_ACCOUNT"
    password = "YOUR_FACEBOOK_PASSWORD"
    message = "I would like to share this repo:\nhttps://github.com/wuduhren/fb-group-auto-posting\nIt can help you share your content!"

    # Groups you have posting access
    groups = [
        "https://www.facebook.com/groups/pythontw",
        "https://www.facebook.com/groups/automationtesting.selenium/",
        "https://www.facebook.com/groups/340297793126328"
    ]


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    # chrome_options.add_argument("-headless")
    chrome_options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.notifications": 2  # 1:allow, 2:block
    })

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(15)  # seconds

    # Go to facebook.com
    driver.get("http://www.facebook.com")

    # Enter user account
    elem = driver.find_element_by_id("email")
    elem.send_keys(account)

    # Enter user password
    elem = driver.find_element_by_id("pass")
    elem.send_keys(password)

    # Login
    elem.send_keys(Keys.RETURN)
    sleep(1)

    for group in groups:

        # Go to the Facebook Group
        driver.get(group)
        sleep(2)

        # Click the post box
        post_area = driver.find_elements_by_xpath("//*[contains(text(), 'on your mind')]")[0]
        post_area.click()
        sleep(1)

        # Message input
        post_box = driver.switch_to.active_element
        post_box.send_keys(message)
        sleep(1)

        # Post
        button = driver.find_elements_by_xpath("//*[text()='Post']")[0]
        button.click()
        sleep(1)

    driver.close()


if __name__ == '__main__':
    main()
