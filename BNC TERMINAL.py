
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


driver.get('https://info.bct2-4.com/infoservice/index.html')
driver.maximize_window()
# Find the element you want to click on

element = driver.find_element(By.ID, 'mainframe_vframeset_hframeset_bodyframe_introframe_popNotice_titlebar_closebuttonAlignImageElement')

driver(quit())


#mainframe_vframeset_hframeset_bodyframe_workframe_IST010_form_div_work_div_background_Grid00

#<div  style="user-select: none; position: absolute; left: 0px; top: 0px; width: 22px; height: 20px; background-repeat: no-repeat; background-position: center center; background-image: url(&quot;https://info.bct2-4.com/infoservice/img/title_bar_close.png?version=1.0.0&quot;);"></div>