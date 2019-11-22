#Implicit and Explicit Wait

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/home/real/Desktop/Selenium_with_python/SeleniumProjects/chromedriver_linux64/chromedriver")
driver.implicitly_wait(10)
print(driver.title)
driver.get("http://career.eximbankbd.com/Welcome.aspx")
driver.find_element_by_xpath("//*[@id='btnViewLogin']").click()

#assert("Welcome: Mercury Toure") in driver.title

#Wait some time 
 #implicit time in seconds
unm_ele = driver.find_element_by_name("txtLogin")
pass_ele = driver.find_element_by_name("txtPwd")

unm_ele.send_keys("username")
pass_ele.send_keys("password")


driver.find_element_by_xpath("//*[@id='btnLogin']").click()
time.sleep(5)
#driver.quit()#Closes all the browser