from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="/home/real/Desktop/Selenium_with_python/SeleniumProjects/chromedriver_linux64/chromedriver")

driver.get("http://career.eximbankbd.com/Registration.aspx")
print(driver.title)
print(driver.current_url)
driver.close()