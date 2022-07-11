from selenium import webdriver

from time import sleep
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.common.keys import Keys

import pickle






BROWSER_EXE = "C:/Program Files/Mozilla Firefox/firefox.exe"
GECKODRIVER = "C:/Users/Admin/Desktop/gecko/geckodriver.exe"
FIREFOX_BINARY = FirefoxBinary(BROWSER_EXE)
                # webdriver setting
PROFILE = webdriver.FirefoxProfile()

browser = webdriver.Firefox(executable_path=GECKODRIVER,
                                        firefox_binary=FIREFOX_BINARY,
                                        firefox_profile=PROFILE
                                        )


cookies = pickle.load(open("cookies1.pkl", "rb"))
fbUrl = "https://id.zalo.me/account?continue=https%3A%2F%2Fchat.zalo.me%2F"

browser.get(fbUrl)
for cookie in cookies:

   browser.add_cookie(cookie)



login = browser.find_element_by_link_text("VỚI SỐ ĐIỆN THOẠI")

login.click()

sleep(1)



txtUser = browser.find_element_by_id("input-phone")

txtUser.send_keys("0397229040")

sleep(1)



the_css_selector = 'input[tabindex="2"]'

txtPass = browser.find_element_by_css_selector(the_css_selector)

txtPass.send_keys("binhminh123")

sleep(1)



txtPass.send_keys(Keys.ENTER)

sleep(5)