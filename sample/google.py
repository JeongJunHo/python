import time
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")  # Optional argument, if not specified will search path.
driver.get('https://google.com');
# time.sleep(1) # Let the user actually see something!
# driver.find_element_by_xpath('//*[@id="gb_70"]').click()
# driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('jjh49470826@gmail.com')
# driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Ahffk1608!')
# driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
# time.sleep(1)
# time.sleep(10) # Let the user actually see something!