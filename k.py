import os
import platform
import pandas as pd
import time
from selenium import webdriver
from ultis import read_data, write_data
from selenium.webdriver.chrome.options import Options

import pickle

from selenium.webdriver.common.by import By
fbUrl = "https://chat.zalo.me/"
def login(self):
        self.browser.get(self.fbUrl)
        time.sleep(1)
        try: 
            login2 = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[1]/ul/li[2]/a")
            login2.click()
            time.sleep(0.5)
            passEle = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/input')
            passEle.send_keys('binhminh123')
            time.sleep(0.5)
            loginEle = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/div[4]/a')
            time.sleep(0.5)
            loginEle.click()
        except: pass
def load_cookie(self):
        self.fbUrl = "https://chat.zalo.me/"
        self.browser.get(self.fbUrl)
        cookies = pickle.load(open("cookies1.pkl", "rb"))
        for cookie in cookies:
            self.browser.add_cookie(cookie)
        return self.browser
def load_profile(user_data_dir, profile, chrome=True):
    if chrome == True:
        option = Options()
        # option.add_argument("--disable-extensions")
        option.add_argument('--disable-gpu')
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-notifications")

        option.add_argument(f"--profile-directory={profile}")
        option.add_argument(f"--user-data-dir={user_data_dir}")

        option.add_experimental_option("prefs",
                { "profile.default_content_setting_values.notifications": 1}) ## 1 to allow, 2 to block
        option.add_experimental_option('excludeSwitches', ['enable-logging'])

        # logging here
        browser = webdriver.Chrome(executable_path="chromedriver/chromedriver", chrome_options=option)
        return browser

def crawl(self,df_data, i):
        fbid = df_data["new_t"][i]
        try:
            try:  
                inputPhone = self.browser.find_element(By.ID, 'contact-search-input')
                inputPhone.clear()
                inputPhone.send_keys(fbid)
                time.sleep(3)          
                if(self.browser.find_element(By.CLASS_NAME,'conv-item')):
                    a = self.browser.find_element(By.XPATH,"//*[@class='conv-item conv-rel  ']")
                    a.click()
                    time.sleep(1)
                    b = self.browser.find_element(By.ID,'ava_chat_box_view')
                    b.click()
                    time.sleep(1)
                    name = self.browser.find_element(By.CSS_SELECTOR,"div[class='truncate friend-profile__display-name']")
                    df_data["n"][i] = name.text
                    dayOfBirth = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[3]/div/div/div[2]/span[2]')
                    df_data['fb_birthday'][i] = dayOfBirth.text
                    gender = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[3]/div/div/div[1]/span[2]')
                    df_data["gender"][i] = gender.text
                    print(name.text)
                    d = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div[2]/i')
                    time.sleep(0.5)
                    d.click()
                    
                else:
                    pass
            except: pass
        except:
            pass
if __name__ == "__main__":

    input_data_path = f"raw_data/part-01.tsv"
    output_data_path = f"preprocessed_data/part-01.tsv"
    df_data = pd.read_csv(input_data_path, sep ="\t", dtype=str)
    profiles = [
        # 'Default',
        'Profile 1',
        # 'Profile 2',
        # 'Profile 3',
        # 'Profile 4',
        # 'Profile 5',
        # 'Profile 6',
        # 'Profile 7',
        # 'Profile 8',
        # 'Profile 9',
    ]
    browser1 = webdriver.Chrome(executable_path="chromedriver/chromedriver")
    no_profiles = len(profiles)
    if not os.path.exists("preprocessed_data"):
        os.makedirs("preprocessed_data")
    if platform.system() == 'Linux':
        user_data_dir = fr'/home/longvudang/.config/google-chrome'
    for i, row in df_data.iterrows():

        # logging here (logging time for loop and current time)

        profile = profiles[i % no_profiles]

        # chrome=True (default) if crawl with Chrome, False if crawl with Firefox
        
        browser = load_profile(user_data_dir, profile, chrome=True)

        crawl(browser, row, isinstance(browser, webdriver.Chrome))
        if i % 10 == 0:
            write_data(df_data, output_data_path)

        browser.quit()

    write_data(df_data, output_data_path)



