#Explicit Wait(Based on condition)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/real/Desktop/Selenium_with_python/SeleniumProjects/chromedriver_linux64/chromedriver")

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com")



driver.find_element(By.ID, "tab-flight-tab-hp").click()

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("NYC")
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("DAC")


driver.find_element(By.ID, "flight-departing-hp-flight").clear()

driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("01/01/2020")

driver.find_element(By.ID, "flight-returning-hp-flight").clear()

driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("01/05/2020")

driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()
