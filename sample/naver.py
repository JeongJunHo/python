import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")  # Optional argument, if not specified will search path.
driver.get('https://nid.naver.com/nidlogin.login');
time.sleep(1) # Let the user actually see something!
driver.find_element_by_name('id').send_keys('m8907')
time.sleep(1)
pwbox = driver.find_element_by_name('pw').send_keys('ahffk1608!')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(10) # Let the user actually see something!
driver.quit()