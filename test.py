from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://wordpress-automation.000webhostapp.com/wp-admin')

admin = driver.find_element(By.XPATH,'.//*[@id="user_login"]')
admin.send_keys('admin')

password = driver.find_element(By.XPATH,'.//*[@id="user_pass"]')
password.send_keys('wordpress123')

button = driver.find_element(By.XPATH,'.//*[@id="wp-submit"]')
time.sleep(2)
button.click()

time.sleep(2)
driver.get('https://wordpress-automation.000webhostapp.com/wp-admin/post-new.php')

title = driver.find_element(By.XPATH,'.//*[@id="post-title-0"]') 
title.send_keys('This is a test. #3')
sleep(2)

''' to-do: make post message available to automate, block id changes every time
post = driver.find_element_by_css_selector('p.rich-text.block-editor-rich-text__editable.wp-block-paragraph')
post.send_keys('Sent by Selenium Webdriver, Peterzig 2020-04-01.')
sleep(2)'''

publish = driver.find_element(By.XPATH,'//*[@id="editor"]/div/div/div[1]/div/div[1]/div/div[2]/button[2]')
sleep(2)
publish.click()

publish2 = driver.find_element(By.XPATH,'//*[@id="editor"]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div[1]/div/button')
sleep(2)
publish2.click()