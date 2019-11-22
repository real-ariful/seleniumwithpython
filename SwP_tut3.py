from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/home/real/Desktop/Selenium_with_python/SeleniumProjects/chromedriver_linux64/chromedriver")

driver.get("http://career.eximbankbd.com/Welcome.aspx")

print(driver.title)#returns the title of the page
print(driver.current_url)# returns the current url of the page


driver.find_element_by_xpath("//*[@id='btnRegistration']").click()
time.sleep(5)

#driver.close()#Closes currently focused browser

driver.quit()#Closes all the browser