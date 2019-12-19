import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = "http://www.naver.com/"

service = Service('./chromedriver_linux64/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
# URL 읽어 들이기
driver.get(url)
# 브라우저 종료하기
driver.quit()