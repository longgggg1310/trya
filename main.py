from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pickle
import random
from ultis import read_data, write_data
import time
from selenium.webdriver.common.keys import Keys
import timeit
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


import pandas as pd
fbUrl = "https://chat.zalo.me/"
# def get_proxies(browser):
    
#     option = Options()
    
#     browser.get("http://free-proxy-list.net")
#     time.sleep(1)
#     row = int(random.randint(1, 250))
#     ip = browser.find_element(By.XPATH,("//tbody/tr[{row}]/td[1]".format(row=row))).text
#     port = browser.find_element(By.XPATH,("//tbody/tr[{row}]/td[2]".format(row=row))).text

#     proxy = f"{ip}:{port}"
#     # print(proxy)
#     option.add_argument(f'--proxy-server=http://%{proxy}')
#     return browser

class Zalo:
    def __init__(self, depth=1):
        self.browser = webdriver.Chrome(executable_path="chromedriver/chromedriver")
        self.fbUrl = "https://chat.zalo.me/"
        self.depth = depth
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
        cookies = pickle.load(open("cookies2.pkl", "rb"))
        for cookie in cookies:
            self.browser.add_cookie(cookie)
        return self.browser
    
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
                    if not b: df_data['zalo_used'][i] = 'no'
                    else: df_data['zalo_used'][i] = 'yes'
                    b.click()
                    time.sleep(1)
                    wait = WebDriverWait(self.browser, 2)
                    name=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='truncate friend-profile__display-name']")))
                    df_data["n"][i] = name.text
                    dayOfBirth = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[3]/div/div/div[2]/span[2]')
                    df_data['fb_birthday'][i] = dayOfBirth.text
                    gender = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[3]/div/div/div[1]/span[2]')
                    df_data["gender"][i] = gender.text
                    print(name.text)
                    d = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div[2]/i')
                    time.sleep(0.5)
                    d.click()
                else:pass
            except: pass
        except:
            pass
    


if __name__ == '__main__':

    zalo = Zalo(depth=1)
    # get_proxies(browser)
    
    time.sleep(1)
    df_data = pd.read_csv('raw_data/part-01.tsv', sep = '\t', dtype=str)
    df_data["zalo_used"] = "no"
    df_data = df_data[['fbid','n','gender','fb_birthday','new_t','zalo_used']]
    # df_data.rename(columns = {'n':'zalo_name', 'fb_birthday':'zalo_birthday','new_t':'telephone'}, inplace = True)
    start = timeit.default_timer()

    for i in range(101):
        if(i%5==0):
            zalo.browser.close()
            zalo.browser = webdriver.Chrome(executable_path="chromedriver/chromedriver")
            zalo.browser.refresh()
        zalo.load_cookie()
        zalo.login()
        time.sleep(0.5)
        zalo.crawl(df_data, i)
        if (i%2==0):
            write_data(df_data,"preprocessed_data/1.tsv")  
        print(i)
        if(i%5==0):
            zalo.browser.close()
            zalo.browser = webdriver.Chrome(executable_path="chromedriver/chromedriver")
    df_data.rename(columns = {'n':'zalo_name', 'fb_birthday':'zalo_birthday','new_t':'telephone'}, inplace = True)

    write_data(df_data,"preprocessed_data/1.tsv")   
    stop = timeit.default_timer()
    print('Time: ', stop - start)  

 
    # df_data = df_data[['fbid','n','gender','fb_birthday','new_t']]
    # df_data.to_csv (r'preprocessed_data/1.csv', index = None) 
# /html/body/div[1]/div/div/div[2]/div[2]/div[1]/ul/li[2]