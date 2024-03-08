import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://www.speedtest.pl/')
ok_button = driver.find_element(By.CLASS_NAME,'fc-button-label')
ok_button.click()
time.sleep(3)
start_button = driver.find_element(By.XPATH,'//*[@id="tester"]/div[1]/div/div')
start_button.click()
time.sleep(60)
download_data = driver.find_element(By.XPATH,'/html/body/div/main/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div/span')
upload_data = driver.find_element(By.XPATH,'/html/body/div/main/div/div[2]/div[2]/div[1]/div/div[3]/div[4]/div/span')

print(download_data.text,upload_data.text)
internet_speed = float(download_data.text)
