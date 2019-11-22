#Navigation Commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/home/real/Desktop/Selenium_with_python/SeleniumProjects/chromedriver_linux64/chromedriver")


driver.get("http://www.google.com")
print(driver.title)
time.sleep(5)

driver.get("http://www.facebook.com")
print(driver.title)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)


print(driver.title)
#driver.quit()#Closes all the browser