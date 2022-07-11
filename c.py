import pickle
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver/chromedriver")
driver.get("https://chat.zalo.me/")
time.sleep(2)

# login1 =driver.find_element(By.CLASS_NAME,'btnLogin')
login1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[2]/div[1]/ul/li[2]/a')
time.sleep(2)

login1.click()
# time.sleep(3)
# login2 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div[1]/ul/li[2]")
# time.sleep(3)
# login2.click()


userEle =driver.find_element(By.ID,'input-phone')

userEle.send_keys('0978485490')
time.sleep(2)
passEle = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/input')
passEle.send_keys('dong0909')
time.sleep(2)
loginEle = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/div[4]/a')
time.sleep(2)
loginEle.click()
time.sleep(15)

pickle.dump( driver.get_cookies() , open("cookies2.pkl","wb"))