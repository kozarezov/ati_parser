from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import time, sleep
import traceback
import os
import datetime

from config import PASSWORD, LOGIN

def open_webdriver(url):
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized') 
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36') 
    chrome_options.add_argument('origin=https://loads.ati.su') 
    chrome_options.add_argument('referer=https://loads.ati.su')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver = autorizaite(driver)
    #driver.get(url)
    sleep(2)
    return driver

def autorizaite(driver):
    auth = 'https://id.ati.su/login/'
    username = LOGIN
    password = PASSWORD
    driver.get(auth)
    wait = WebDriverWait(driver, 500)
    wait.until(EC.element_to_be_clickable((By.ID, "login")))

    log = driver.find_element(By.ID, 'login').send_keys(username)
    pswd = driver.find_element(By.ID, 'password').send_keys(password)
    sleep(0.2)
    enter = driver.find_element(By.ID, 'action-login').send_keys(Keys.ENTER)
    sleep(3)
    key = input(str)
    code = driver.find_element(By.CLASS_NAME, '_1tVEr-2-0-741').send_keys(key)
    sleep(0.2)
    #enter_code = driver.find_element(By.CLASS_NAME, 'ati-core-button ati-primary').send_keys(Keys.ENTER)
    sleep(3)
    return driver

def move_parsing(driver = None):

    url = 'https://trucks.ati.su/?FromGeo=2_120&fromRegionId=40&ToGeo=2_3611&toRegionId=151'
    if driver == None:
        driver = open_webdriver(url)

if __name__ == "__main__":
    move_parsing()