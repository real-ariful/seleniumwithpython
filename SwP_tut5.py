#Conditional Commands
#is_displayed()
#is_enable()
#is_selected()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/home/real/Desktop/Selenium_with_python/SeleniumProjects/chromedriver_linux64/chromedriver")


driver.get("http://career.eximbankbd.com/Welcome.aspx")

driver.find_element_by_xpath("//*[@id='btnViewLogin']").click()

unm_ele = driver.find_element_by_name("txtLogin")
pass_ele = driver.find_element_by_name("txtPwd")

print(unm_ele.is_displayed())# Return displayed or not
print(unm_ele.is_enabled())#Returns enabled or not
print(pass_ele.is_displayed())# Return displayed or not
print(pass_ele.is_enabled())#Returns enabled or not

unm_ele.send_keys("username")
pass_ele.send_keys("password")


driver.find_element_by_xpath("//*[@id='btnLogin']").click()
time.sleep(5)
#driver.quit()#Closes all the browser