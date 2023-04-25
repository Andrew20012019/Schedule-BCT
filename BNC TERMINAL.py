from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


# BNC TERMINAL
# Send a GET request to the website you want to scrape
url = "https://info.bct2-4.com/infoservice/index.html"
driver=webdriver.Chrome()
driver.get(url)
element = driver.find_element(By.ID, "mainframe_vframeset_hframeset_bodyframe_introframe_popNotice_titlebar_closebuttonAlignImageElement")

element.click()

driver.quit()

